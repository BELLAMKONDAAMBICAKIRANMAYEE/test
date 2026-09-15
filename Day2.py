from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import datetime

app = FastAPI(title="Day-2")

jobs: dict = {}
count = 1


class CREATEJOB(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    role: str
    min_salary: int = Field(ge=100, le=500)
    max_salary: int = Field(ge=100, le=500)


@app.get("/")
def index():
    return {"Day-2": "content"}


@app.post("/jobs/")
def createjob(payload: CREATEJOB):
    global count

    job = {
        "id": count,
        **payload.model_dump(),
        "is_active": True,
        "Created_at": datetime.now()
    }

    jobs[count] = job
    count += 1

    return job


@app.get("/jobs/")
def jobs_list():
    return list(jobs.values())