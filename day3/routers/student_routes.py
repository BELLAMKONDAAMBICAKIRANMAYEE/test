from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Student
from schemas import CreateStudents, StudentResponse


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

# CREATE STUDENT
@router.post(
    "/",
    response_model=StudentResponse,
    status_code=201
)
def create_student(
    payload: CreateStudents,
    db: Session = Depends(get_db)
):

    student = Student(
        **payload.model_dump()
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    return student


# GET ALL STUDENTS
@router.get(
    "/",
    response_model=list[StudentResponse]
)
def get_students(
    db: Session = Depends(get_db)
):

    return db.query(Student).all()


# GET SINGLE STUDENT
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
        .filter(Student.id == student_id)
        .first()
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student