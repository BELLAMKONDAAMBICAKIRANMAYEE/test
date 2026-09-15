from fastapi import APIRouter
from datetime import datetime
from models import Job
from schemas import CreateJob, UpdateJob
from sqlalchemy.orm import Session
from pagination import get_db

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


# CREATE JOB
@router.post("/",response_model=JobResponse,status_code=201)
def createjob(payload: CreateJob,db:Session=Depends(get_db)):
     record=Job(**jobdata.model_dum())
     db.ass(record)
     db.commit()
     db.refresh(record)
     return record



    # global count

    # job = {
    #     "id": count,
    #     **payload.model_dump(),
    #     "is_active": True,
    #     "Created_at": datetime.now()
    # }

    # # jobs[count] = job

    # # count += 1

    # return job


# GET ALL JOBS
# @router.get("/")
# def jobs_list():

#     return list(jobs.values())


# # GET SINGLE JOB
# @router.get("/{job_id}")
# def get_job(job_id: int):
#     if job_id not in jobs:
#             return {
#                 "message": "Job not found"
#             }
#     return jobs.get(job_id)

   


# # UPDATE JOB
# @router.put("/{job_id}")
# def update_job(
#     job_id: int,
#     payload: UpdateJob
# ):

#     if job_id not in jobs:
#         return {
#             "message": "Job not found"
#         }

#     update_data = payload.model_dump(
#         exclude_unset=True
#     )

#     jobs[job_id].update(update_data)

#     return jobs[job_id]


# # DELETE JOB
# @router.delete("/{job_id}")
# def delete_job(job_id: int):

#     if job_id not in jobs:
#         return {
#             "message": "Job not found"
#         }

#     deleted_job = jobs.pop(job_id)

#     return {
#         "message": "Job deleted successfully",
#         "job": deleted_job
#     }