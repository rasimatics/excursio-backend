from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError
from starlette.middleware.cors import CORSMiddleware
from os import makedirs

from .core.config.settings import app_settings
from .core.exceptions.repo import RepoException
from .core.exceptions.service import ServiceException
from .core.exceptions.http import CustomHTTPException
from .core.exceptions import handlers
from .apps._main.routes import router
from .di import AllContainers


def create_app():
    app = FastAPI(**app_settings.dict())
    
    # add all dependencies
    container = AllContainers()
    app.container = container
    
    # add all routes
    app.include_router(router)

    # pydantic validation errors
    app.add_exception_handler(RequestValidationError, handlers.validation_exception_handler)
    
    # repository errors
    app.add_exception_handler(RepoException, handlers.handle_repo_exceptions)    

    # service errors
    app.add_exception_handler(ServiceException, handlers.handle_service_exceptions)

    # http errors
    app.add_exception_handler(CustomHTTPException, handlers.handle_http_exceptions)

    # unhandled errors
    app.add_exception_handler(Exception, handlers.handle_global_exceptions)


    # add middlewares
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=["*"] if app_settings.DEBUG else app_settings.ALLOWED_HOSTS,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    makedirs("media", exist_ok=True)
    app.mount("/media", StaticFiles(directory=app_settings.MEDIA_FOLDER), name="media")


    return app


app = create_app()
