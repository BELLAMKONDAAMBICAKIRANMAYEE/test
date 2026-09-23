from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker
)


# =========================
# SYNC DATABASE
# =========================

DATABASE_URL = "mysql+pymysql://root:admin@localhost/ats_db"

engine = create_engine(
    DATABASE_URL,
    echo=True
)

LocalSession = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


# =========================
# ASYNC DATABASE
# =========================

ASYNC_DATABASE_URL = (
    "mysql+asyncmy://root:admin@localhost/ats_db"
)

async_engine = create_async_engine(
    ASYNC_DATABASE_URL,
    echo=True
)

AsyncLocalSession = async_sessionmaker(
    bind=async_engine,
    autoflush=False,
    expire_on_commit=False
)


# =========================
# BASE
# =========================

class Base(DeclarativeBase):
    pass