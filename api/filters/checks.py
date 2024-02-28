from datetime import date
from typing import Optional
from pydantic import Field

from fastapi import Query

from models.checks import PaymentTypeEnum

from utils.filters import BaseFilterModel

from settings import query_filters_settings


class CheckFilter(BaseFilterModel):
    filter__total__gte: Optional[int] = Query(None)
    filter__total__lte: Optional[int] = Query(None)
    filter__created_at__gte: Optional[date] = Field(
        Query(None, description=f'Correct timer format is {query_filters_settings.DEFAULT_DATE_FORMAT}')
    )
    filter__created_at__lte: Optional[date] = Field(
        Query(None, description=f'Correct timer format is {query_filters_settings.DEFAULT_DATE_FORMAT}')
    )
    filter__payment_type__eq: PaymentTypeEnum | None = Query(None)
