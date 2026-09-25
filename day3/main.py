from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from models import Job, Student, Application

from routers.job_router import router as job_router
from routers.student_routes import router as student_router
from routers.application_routes import router as application_router
from routers.auth_router import router as auth_router
from middleware.logs_middleware import LoggingMiddleware
from utils.logger import get_logger


Base.metadata.create_all(bind=engine)

logger=get_logger("main")

app = FastAPI(
    title="Day-3"
)



# =========================
# CORS CONFIGURATION
#cors allowed API Calls
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],#post,put,delete,patch,get
    allow_headers=["*"],
)


#request response logs
app.add_middleware(LoggingMiddleware)

#Error handlers
@app.exception_handler(Exception)
async def global_exception_handler(request:Request,exc:Exception):
    logger.error(f"Unhandled Errors on{request.method} {request.url.path} {exc}")
    return JSONResponse(status_code=500,
        content={"details":"Internal Server Error"}
    )

# =========================
# ROUTERS
# =========================

app.include_router(job_router)
app.include_router(student_router)
app.include_router(application_router)
app.include_router(auth_router)

@app.get("/")
def health():
    return {"message": "app running properly..."}