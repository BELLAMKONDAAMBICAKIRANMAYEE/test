from fastapi import FastAPI

from database import engine, Base
from models import Job, Student

from routers.job_router import router as job_router
from routers.student_routes import router as student_router

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Day-3"
)


@app.get("/")
def health():
    return {
        "message": "app running properly"
    }


app.include_router(job_router)
app.include_router(student_router)