from fastapi import Query

def jobs_pagination(
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

