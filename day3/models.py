from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from datetime import datetime

from database import Base


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