from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


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