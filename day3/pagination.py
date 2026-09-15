from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session

from database import LocalSession
from models import Job


router = APIRouter(
    prefix="/pagination",
    tags=["Paginations by pardhu"]
)


def get_db():

    db = LocalSession()

    try:
        yield db

    finally:
        db.close()


@router.get("/jobs")
def jobs_pagination(
    skip: int = Query(
        default=0,
        ge=0
    ),

    limit: int = Query(
        default=10,
        ge=1,
        le=100
    ),

    db: Session = Depends(get_db)
):

    job_list = (
        db.query(Job)
        .offset(skip)
        .limit(limit)
        .all()
    )

    return job_list