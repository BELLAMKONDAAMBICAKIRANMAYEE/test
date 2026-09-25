import bcrypt
import os
#JOSE in jwt
from jose import jwt,JWTError
# from dotenv import getenv
from datetime import datetime,timedelta
from dotenv import load_dotenv
from os import getenv

load_dotenv()

SECRET=os.getenv("SECRET")#os getenv(secret_key)
ALGORITHM=os.getenv("ALGORITHM","HS256")
#ALGORTHIMS LIST
EXPIRE_MINUTES=os.getenv("EXPIRE_MINUTES",60)

def hash_password(plain:str):
    return bcrypt.hashpw(plain.encode(),bcrypt.gensalt()).decode()

def verify_password(plain:str,hashed:str):
    return bcrypt.checkpw(plain.encode(),hashed.encode())



def create_token(user_id:int,role:str):
    payload={
        "sub":str(user_id),
        "role":role,
        "exp":datetime.utcnow()+timedelta(minutes=EXPIRE_MINUTES)
    }
    return jwt.encode(payload,SECRET,algorithm=ALGORITHM)

def decode_token(token:str):
    return jwt.decode(token,SECRET,algorithms=[ALGORITHM])
