from sqlalchemy.orm import Session
from fastapi import FastAPI,Depends,HTTPException
from models import User
from schemas import Register,Login,TokenResponse
from utils.security import create_token, hash_password,verify_password

def register_user(payload:Register,db:Session):
    existing=db.query(User).filter(User.email==payload.email).first()
    if existing:
        raise HTTPException(detail="Email already registered",status_code=409)
    
    user=User(name=payload.name,email=payload.email,hashed_pwd=hash_password(payload.password),
              role=payload.role)
    db.add(user)
    db.commit()
    return {"message":"Registered Successfully"}

def login_user(payload:Login,db:Session):
    #user must exist
    user=db.query(User).filter(User.email==payload.email).first()
    if not user:
        raise HTTPException(status_code=401,detail="Invalid Username or Password")
    #password must match
    if not verify_password(payload.password,user.hashed_pwd):
        raise HTTPException(detail="Invalid email or password",status_code=401)

    token=create_token(user.id,user.role)
    return {"access_token":token,"token_type":"bearer"}

    
    

