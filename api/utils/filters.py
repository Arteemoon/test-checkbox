from datetime import datetime, date
from enum import Enum
from pydantic import BaseModel

from tortoise.queryset import QuerySet
from tortoise.expressions import Q


from settings import query_filters_settings


OPTIONS_MAPPING = {
    "eq": "",
    "gte": "__gte",
    "lte": "__lte",
}


class FilterSet:
    """Warning! support format for filter name is 'filter__{field_name}__{option}'
    Example filter__created_at__gte is orm used as .filter(Q(created_at__gte=value))
    it's minimal functional for used for this project
    """

    def __init__(self, queryset: QuerySet, filters: BaseModel):
        self.queryset = queryset
        self.filters = filters

    def apply(self):
        for filter_key, filter_value in self.filters.model_dump().items():
            if filter_key.startswith("filter__") and filter_value is not None:
                _, field_name, option = filter_key.split("__")
                if isinstance(filter_value, Enum):
                    filter_value = filter_value.value
                self.queryset = self.queryset.filter(Q(**{f"{field_name}{OPTIONS_MAPPING.get(option)}": filter_value}))

        return self.queryset


class BaseFilterModel(BaseModel):

    class Config:
        # Set your custom datetime format here
        json_encoders = {
            datetime: lambda v: v.strftime(query_filters_settings.DEFAULT_DATETIME_FORMAT),
            date: lambda v: v.strftime(query_filters_settings.DEFAULT_DATE_FORMAT),
        }
