from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependency import get_db, pagination
from models import Student
from schemas import (
    CreateStudents,
    UpdateStudents,
    StudentResponse
)


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


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


@router.get(
    "/",
    response_model=list[StudentResponse]
)
def get_students(
    pages: dict = Depends(pagination),
    db: Session = Depends(get_db)
):

    return (
        db.query(Student)
        .offset(pages["skip"])
        .limit(pages["limit"])
        .all()
    )


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
        .filter(Student.id == student_id)
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
        setattr(student, key, value)

    db.commit()
    db.refresh(student)

    return student


@router.delete("/{student_id}")
def delete_student(
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

    db.delete(student)
    db.commit()

    return {
        "message": "Student deleted successfully",
        "student_id": student_id
    }