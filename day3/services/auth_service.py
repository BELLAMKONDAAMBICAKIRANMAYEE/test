from sqlalchemy.orm import Session
from fastapi import FastAPI,Depends,HTTPException
from models import User
from schemas import Register
from utils.security import create_token

def register_user(payload:Register,db:Session):
    existing=db.query(User).filter(User.email==payload.email).first()
    if existing:
        raise HTTPException(detail="Email already registered",status_code=409)
    
    user=User(name=payload.name,email=payload.email,hashed_pwd=payload.password,
              role=payload.role)
    db.add(user)
    db.commit()
    return {"message":"Registered Successfully"}