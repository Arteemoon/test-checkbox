from fastapi import status, HTTPException

from tortoise.exceptions import DoesNotExist


def object_not_found_handler(_, exc: DoesNotExist):
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Object not found",
    )
