from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    DateTime,
    ForeignKey,
    UniqueConstraint
)
from datetime import datetime
from sqlalchemy.orm import relationship
from database import Base


class Student(Base):

    __tablename__ = "students"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(150),
        nullable=False
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False
    )

    phone = Column(
        String(13),
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.now
    )

    applications = relationship(
        "Application",
        back_populates="student"
    )


class Job(Base):

    __tablename__ = "jobs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(20),
        nullable=False
    )

    role = Column(
        String(30),
        nullable=False
    )

    min_salary = Column(
        Float,
        nullable=False
    )

    max_salary = Column(
        Float,
        nullable=False
    )

    is_active = Column(
        Boolean,
        default=True
    )

    created_at = Column(
        DateTime,
        default=datetime.now
    )

    applications = relationship(
        "Application",
        back_populates="job"
    )


class Application(Base):

    __tablename__ = "applications"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    student_id = Column(
        Integer,
        ForeignKey("students.id"),
        nullable=False
    )

    job_id = Column(
        Integer,
        ForeignKey("jobs.id"),
        nullable=False
    )

    status = Column(
        String(50),
        default="applied"
    )

    applied_at = Column(
        DateTime,
        default=datetime.now
    )

    student = relationship(
        "Student",
        back_populates="applications"
    )

    job = relationship(
        "Job",
        back_populates="applications"
    )

    __table_args__ = (
        UniqueConstraint(
            "student_id",
            "job_id",
            name="uq_student_job"
        ),
    )