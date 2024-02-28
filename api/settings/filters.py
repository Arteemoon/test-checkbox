from pydantic import BaseModel


class QueryFilterSettings(BaseModel):
    DEFAULT_DATETIME_FORMAT: str = '%Y-%m-%d %H:%M'
    DEFAULT_DATE_FORMAT: str = '%Y-%m-%d'
