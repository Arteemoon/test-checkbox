from fastapi import FastAPI
from utils.lifespan import lifespan

from routers import auth, checks

from settings import application_settings

from utils.exception_handlers import EXCEPTION_HANDLERS


def get_asgi_application():
    app = FastAPI(
        lifespan=lifespan,
        docs_url=application_settings.DOCS_URL,
        version=application_settings.VERSION,
        root_path=application_settings.ROOT_PATH,
    )
    app.include_router(auth.router)
    app.include_router(checks.router)
    app.exception_handlers.update(EXCEPTION_HANDLERS)
    # include middlewares and more
    return app


app = get_asgi_application()
