from tortoise.queryset import QuerySet

from schemas.pagination import PaginationQueryParamsSchema


class Paginator:
    """Basic implementation of tortoise paginator"""

    def __init__(
        self, queryset: QuerySet, query_params: PaginationQueryParamsSchema
    ) -> None:
        self.queryset = queryset
        self.query_params = query_params

    def paginate(self) -> QuerySet:
        return self.queryset.offset(self.query_params.offset).limit(
            self.query_params.limit
        )


def get_paginated_response(data: list[dict], limit: int, offset: int) -> dict:
    return {
        "data": data,
        "meta": {
            "limit": limit,
            "offset": offset,
        },
    }
