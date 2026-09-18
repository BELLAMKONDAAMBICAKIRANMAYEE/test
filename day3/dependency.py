from fastapi import Query
from database import LocalSession


def get_db():

    db = LocalSession()

    try:
        yield db

    finally:
        db.close()


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