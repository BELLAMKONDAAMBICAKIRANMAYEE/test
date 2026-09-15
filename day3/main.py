from fastapi import FastAPI
from Day3 import router as job_router
from pagination import router as pagination_router


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