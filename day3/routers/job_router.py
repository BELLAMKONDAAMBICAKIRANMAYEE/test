from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from dependency import get_async_db, pagination, require_role
from models import Job
from schemas import CreateJob, UpdateJob, JobResponse


router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


# =========================
# CREATE
# =========================

@router.post(
    "/",
    response_model=JobResponse,
    status_code=201
)
async def createjob(
    payload: CreateJob,
    db: AsyncSession = Depends(get_async_db),
    current_user=Depends(require_role("admin", "recruiter"))
):

    record = Job(
        **payload.model_dump()
    )

    db.add(record)

    await db.commit()
    await db.refresh(record)

    return record


# =========================
# GET ALL + PAGINATION
# =========================

@router.get(
    "/",
    response_model=list[JobResponse]
)
async def jobs_list(
    pages: dict = Depends(pagination),
    db: AsyncSession = Depends(get_async_db)
):

    result = await db.execute(
        select(Job)
        .offset(pages["skip"])
        .limit(pages["limit"])
    )

    return result.scalars().all()


# =========================
# GET SINGLE
# =========================

@router.get(
    "/{job_id}",
    response_model=JobResponse
)
async def get_job(
    job_id: int,
    db: AsyncSession = Depends(get_async_db)
):

    result = await db.execute(
        select(Job).where(
            Job.id == job_id
        )
    )

    job = result.scalar_one_or_none()

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    return job


# =========================
# UPDATE
# =========================

@router.put(
    "/{job_id}",
    response_model=JobResponse
)
async def update_job(
    job_id: int,
    payload: UpdateJob,
    db: AsyncSession = Depends(get_async_db),
    current_user=Depends(require_role("admin"))
):

    result = await db.execute(
        select(Job).where(
            Job.id == job_id
        )
    )

    job = result.scalar_one_or_none()

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

    await db.commit()
    await db.refresh(job)

    return job


# =========================
# DELETE
# =========================

@router.delete("/{job_id}")
async def delete_job(
    job_id: int,
    db: AsyncSession = Depends(get_async_db),
    current_user=Depends(require_role("admin"))
):

    result = await db.execute(
        select(Job).where(
            Job.id == job_id
        )
    )

    job = result.scalar_one_or_none()

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    await db.delete(job)
    await db.commit()

    return {
        "message": "Job deleted successfully",
        "job_id": job_id
    }