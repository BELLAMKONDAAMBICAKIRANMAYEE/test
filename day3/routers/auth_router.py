from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import Register,Login
from dependency import get_db
from services import auth_service

router=APIRouter(prefix="/auth",tags=["Auth"])

@router.post("/register",status_code=201)
def register(payload:Register,db:Session=Depends(get_db)):
    return auth_service.register_user(payload,db)


@router.post("/login")
def login(payload:Login,db:Session=Depends(get_db)):
    return auth_service.login_user(payload,db)




