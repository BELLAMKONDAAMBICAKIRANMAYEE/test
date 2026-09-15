from fastapi import APIRouter, Query
from database import LocalSession
from Day3 import jobs


router = APIRouter(
    prefix="/pagination",
    tags=["Paginations by pardhu"]
)

def get_db():
    db=LocalSession()
    try:
        yield db
    finally:
        db.close()

  

@router.get("/jobs")
def jobs_pagination(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):

    job_list = list(jobs.values())

    return job_list[skip:skip + limit]