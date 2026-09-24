from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


# =========================
# JOB SCHEMAS
# =========================

class CreateJob(BaseModel):

    name: str = Field(
        min_length=3,
        max_length=20
    )

    role: str = Field(
        min_length=2,
        max_length=30
    )

    min_salary: int = Field(
        ge=100,
        le=500
    )

    max_salary: int = Field(
        ge=100,
        le=500
    )


class UpdateJob(BaseModel):

    name: Optional[str] = Field(
        default=None,
        min_length=3,
        max_length=20
    )

    role: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=30
    )

    min_salary: Optional[int] = Field(
        default=None,
        ge=100,
        le=500
    )

    max_salary: Optional[int] = Field(
        default=None,
        ge=100,
        le=500
    )


class JobResponse(BaseModel):

    id: int
    name: str
    role: str
    min_salary: float
    max_salary: float
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


# =========================
# STUDENT SCHEMAS
# =========================

class CreateStudents(BaseModel):

    name: str = Field(
        min_length=3,
        max_length=150
    )

    email: str

    phone: str = Field(
        min_length=10,
        max_length=13
    )


class StudentResponse(BaseModel):

    id: int
    name: str
    email: str
    phone: str
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )

class UploadResumeResponse(BaseModel):
    student_id:int
    filename:str
    message:str

class UpdateStudents(BaseModel):

    name: Optional[str] = Field(
        default=None,
        min_length=3,
        max_length=150
    )

    email: Optional[str] = None

    phone: Optional[str] = Field(
        default=None,
        min_length=10,
        max_length=13
    )
class CreateApplication(BaseModel):
    student_id:int
    job_id:int

#applications schema

class ApplicationResponse(BaseModel):
    id:int
    student_id:int
    job_id:int
    status:str
    applied_at:datetime

#users schema
class Register(BaseModel):
    name:str=Field(min_length=2,max_length=150)
    email:str=Field(min_length=5)
    password:str=Field(min_length=6)
    role:str="student"


#login user
class Login(BaseModel):
    email:str
    password:str

class TokenResponse(BaseModel):
    acess_token:str
    token_type:str="bearer"


