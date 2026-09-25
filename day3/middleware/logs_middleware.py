from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request 
from utils.logger import get_logger
import time

logger=get_logger("request")

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request:Request, call_next):
        start=time.time()
        response=await call_next(request)
        duration=(time.time()-start)*1000
        logger.info(f"{request.method}{request.url.path}{response.status_code}{duration}")
        return response




        