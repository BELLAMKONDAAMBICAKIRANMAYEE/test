
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import aiofiles
import os

from dependency import (
    get_db,
    get_async_db,
    pagination,
    require_role
)

from models import Student

from schemas import (
    CreateStudents,
    UpdateStudents,
    StudentResponse,
    UploadResumeResponse
)


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


# ============================================================
# RESUME CONFIGURATION
# ============================================================

ALLOWED_TYPES = {
    "application/pdf",
    "image/jpeg",
    "image/png"
}

UPLOAD_DIR = "uploads"


# ============================================================
# CREATE STUDENT
# ============================================================

@router.post(
    "/",
    response_model=StudentResponse,
    status_code=201
)
def create_student(
    payload: CreateStudents,
    db: Session = Depends(get_db),
    _=Depends(require_role("recruiter"))
):

    student = Student(
        **payload.model_dump()
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    return student


# ============================================================
# UPLOAD RESUME
# ============================================================

@router.post(
    "/{student_ID}/resume",
    response_model=UploadResumeResponse,
    status_code=201
)
async def upload_resume(
    student_ID: int,
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_async_db)
):

    # --------------------------------------------------------
    # 1. Find student
    # --------------------------------------------------------

    result = await db.execute(
        select(Student).where(
            Student.id == student_ID
        )
    )

    student = result.scalar_one_or_none()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # --------------------------------------------------------
    # 2. Validate file type
    # --------------------------------------------------------

    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, JPEG and PNG files are allowed"
        )

    # --------------------------------------------------------
    # 3. Create upload directory
    # --------------------------------------------------------

    os.makedirs(
        UPLOAD_DIR,
        exist_ok=True
    )

    # --------------------------------------------------------
    # 4. Create filename
    # --------------------------------------------------------

    filename = f"student_{student_ID}_{file.filename}"

    # --------------------------------------------------------
    # 5. Create complete file path
    # --------------------------------------------------------

    file_path = os.path.join(
        UPLOAD_DIR,
        filename
    )

    # --------------------------------------------------------
    # 6. Save uploaded file
    # --------------------------------------------------------

    async with aiofiles.open(
        file_path,
        "wb"
    ) as f:

        content = await file.read()

        await f.write(content)

    # --------------------------------------------------------
    # 7. Save file path in database
    # --------------------------------------------------------

    student.resume_path = file_path

    await db.commit()

    await db.refresh(student)

    # --------------------------------------------------------
    # 8. Return response
    # --------------------------------------------------------

    return UploadResumeResponse(
        student_id=student_ID,
        filename=filename,
        message="Resume Uploaded Successfully"
    )


# ============================================================
# GET ALL STUDENTS
# ============================================================

@router.get(
    "/",
    response_model=list[StudentResponse]
)
def get_students(
    pages: dict = Depends(pagination),
    db: Session = Depends(get_db),
    _=Depends(require_role("recruiter"))
):

    students = (
        db.query(Student)
        .offset(pages["skip"])
        .limit(pages["limit"])
        .all()
    )

    return students


# ============================================================
# GET SINGLE STUDENT
# ============================================================

@router.get(
    "/{student_id}",
    response_model=StudentResponse
)
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = (
        db.query(Student)
        .filter(
            Student.id == student_id
        )
        .first()
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# ============================================================
# UPDATE STUDENT
# ============================================================

@router.put(
    "/{student_id}",
    response_model=StudentResponse
)
def update_student(
    student_id: int,
    payload: UpdateStudents,
    db: Session = Depends(get_db)
):

    student = (
        db.query(Student)
        .filter(
            Student.id == student_id
        )
        .first()
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    data = payload.model_dump(
        exclude_unset=True
    )

    for key, value in data.items():
        setattr(
            student,
            key,
            value
        )

    db.commit()

    db.refresh(student)

    return student


# ============================================================
# DELETE STUDENT
# ============================================================

@router.delete(
    "/{student_id}"
)
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = (
        db.query(Student)
        .filter(
            Student.id == student_id
        )
        .first()
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(student)

    db.commit()

    return {
        "message": "Student deleted successfully",
        "student_id": student_id
    }

