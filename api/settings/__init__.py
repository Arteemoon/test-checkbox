from .database import DatabaseSettings
from .auth import AuthSettings
from .application import ApplicationSettings
from .filters import QueryFilterSettings

database_settings = DatabaseSettings()
auth_settings = AuthSettings()
application_settings = ApplicationSettings()
query_filters_settings = QueryFilterSettings()

TORTOISE_ORM_CONF = database_settings.TORTOISE_ORM_CONF  # for accept aerich
