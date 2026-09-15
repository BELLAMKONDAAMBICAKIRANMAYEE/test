from fastapi import FastAPI

from database import engine, Base
from models import Job

from Day3 import router as job_router
from pagination import router as pagination_router


# Create database tables
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
app.include_router(pagination_router)