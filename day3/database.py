from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker
)
import os

load_dotenv()
# =========================
# SYNC DATABASE
# =========================

DATABASE_URL = os.getenv("DATABASE_URL")

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

ASYNC_DATABASE_URL = os.getenv("ASYNC_DATABASE_URL")

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