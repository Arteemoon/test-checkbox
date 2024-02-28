import os
from pydantic import BaseModel


class DatabaseSettings(BaseModel):
    POSTGRES_DATABASE: str = os.environ['POSTGRES_DATABASE']
    POSTGRES_HOST: str= os.environ['POSTGRES_HOST']
    POSTGRES_USER: str = os.environ['POSTGRES_USER']
    POSTGRES_PASSWORD: str = os.environ['POSTGRES_PASSWORD']
    POSTGRES_PORT: str = os.environ['POSTGRES_PORT']
    TORTOISE_ORM_CONF: dict = {
    'connections': {'default': f'postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}'},
    'apps': {
        'models': {
            'models': ['aerich.models', 'models.products', 'models.users'],
            'default_connection': 'default',
            },
        },
    }
