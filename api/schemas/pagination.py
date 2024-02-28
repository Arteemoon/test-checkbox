from fastapi import Query

from pydantic import BaseModel


class PaginationQueryParamsSchema(BaseModel):
    limit: int = Query(default=10, ge=0)
    offset: int = Query(default=0, ge=0)


class PaginatedResponseSchema(BaseModel):
    data: list
    meta: PaginationQueryParamsSchema
