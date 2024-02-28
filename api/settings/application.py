from pydantic import BaseModel


class ApplicationSettings(BaseModel):
    DOCS_URL: str = "/"
    ROOT_PATH: str = "/api/v1"
    VERSION: str = "1.0.0"
