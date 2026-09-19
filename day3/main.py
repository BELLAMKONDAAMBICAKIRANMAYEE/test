from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base
from models import Job, Student, Application

from routers.job_router import router as job_router
from routers.student_routes import router as student_router
from routers.application_routes import router as application_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Day-3"
)


# =========================
# CORS CONFIGURATION
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health():

    return {
        "message": "app running properly"
    }


# =========================
# ROUTERS
# =========================

app.include_router(job_router)
app.include_router(student_router)
app.include_router(application_router)