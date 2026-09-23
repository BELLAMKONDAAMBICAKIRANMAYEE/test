from fastapi import Query
from database import LocalSession,AsyncLocalSession
from utils.security import decode_token
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from models import User

oauth2_schema=OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_db():

    db = LocalSession()

    try:
        yield db

    finally:
        db.close()

#async get_db
async def get_async_db():
    async with AsyncLocalSession() as session:
        yield session


def pagination(
    skip: int = Query(
        default=0,
        ge=0
    ),

    limit: int = Query(
        default=10,
        ge=1,
        le=100
    )
):

    return {
        "skip": skip,
        "limit": limit
    }

def get_create_user(token:str=Depends(oauth2_schema),db:Session=Depends(get_db)):
    try:
        payload=decode_token(token)
    except ValueError:
        raise HTTPException(detail="Invalid Token or Expired Token",status_code=401)

    user=db.query(User).filter(User.id==int(payload["sub"])).first()
    if not user :
        raise HTTPException(status_code=401,detail="user not found or inactive"
                            )
    return user

def require_role(*roles:str):
    def checker(current_user:User=Depends(get_create_user)):
        if current_user.role not in roles:
            raise  HTTPException(
                status_code=403,
                detals=f"Access denied.Required rols:{', '.join(roles)}"
            )
        return current_user
    return checker

async def get_async_db():
    async with AsyncLocalSession() as session:
        yield session