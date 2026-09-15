from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import LocalSession
from models import Job
from schemas import CreateJob, UpdateJob, JobResponse


router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


def get_db():

    db = LocalSession()

    try:
        yield db

    finally:
        db.close()


# CREATE
@router.post(
    "/",
    response_model=JobResponse,
    status_code=201
)
def createjob(
    payload: CreateJob,
    db: Session = Depends(get_db)
):

    record = Job(
        **payload.model_dump()
    )

    db.add(record)

    db.commit()

    db.refresh(record)

    return record


# GET ALL
@router.get(
    "/",
    response_model=list[JobResponse]
)
def jobs_list(
    db: Session = Depends(get_db)
):

    return db.query(Job).all()


# GET SINGLE
@router.get(
    "/{job_id}",
    response_model=JobResponse
)
def get_job(
    job_id: int,
    db: Session = Depends(get_db)
):

    job = (
        db.query(Job)
        .filter(Job.id == job_id)
        .first()
    )

    if job is None:

        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    return job


# UPDATE
@router.put(
    "/{job_id}",
    response_model=JobResponse
)
def update_job(
    job_id: int,
    payload: UpdateJob,
    db: Session = Depends(get_db)
):

    job = (
        db.query(Job)
        .filter(Job.id == job_id)
        .first()
    )

    if job is None:

        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    update_data = payload.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():

        setattr(job, key, value)

    db.commit()

    db.refresh(job)

    return job


# DELETE
@router.delete("/{job_id}")
def delete_job(
    job_id: int,
    db: Session = Depends(get_db)
):

    job = (
        db.query(Job)
        .filter(Job.id == job_id)
        .first()
    )

    if job is None:

        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    db.delete(job)

    db.commit()

    return {
        "message": "Job deleted successfully",
        "job_id": job_id
    }