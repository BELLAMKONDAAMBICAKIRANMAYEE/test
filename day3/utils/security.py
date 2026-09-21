import bcrypt
import os
#JOSE in jwt
from jose import jwt,JWTError
# from dotenv import getenv
from datetime import datetime,timedelta

SECRET="CoDeGnAn2018"#os getenv(secret_key)
ALGORITHM="HS256"
#ALGORTHIMS LIST
EXPIRE_MINUTES=60

def create_token(user_id:int,role:str):
    payload={
        "sub":str(user_id),
        "role":role,
        "exp":datetime.utcnow()+timedelta(minutes=EXPIRE_MINUTES)
    }
    return jwt.encode(payload,SECRET,algorithm=ALGORITHM)
