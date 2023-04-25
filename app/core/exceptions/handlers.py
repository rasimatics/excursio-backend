from dependency_injector.wiring import inject, Provide
from fastapi.responses import JSONResponse
from ..dependency.containers import CoreContainer
from ..response.base import Response

@inject
async def handle_global_exceptions(request, exc, logger = Provide[CoreContainer.app_logger]):  
    """ 
        handling unhandled exceptions   
    """
    response = Response(msg="Unknown exception", is_success=False)
    logger.error(str(exc), extra={"statuscode": 500})
    return JSONResponse(response.dict(), status_code=500)


@inject
async def handle_http_exceptions(request, exc, logger = Provide[CoreContainer.app_logger]):
    """
        handling HTTPException
    """
    response = Response(msg=exc.message, is_success=False)
    logger.error(exc.message, extra={"statuscode":exc.status})
    return JSONResponse(response.dict(), status_code=exc.status)

@inject
async def handle_repo_exceptions(request, exc, logger = Provide[CoreContainer.app_logger]):
    """
        handling RepoException
    """
    response = Response(msg=exc.message, is_success=False)
    logger.error(exc.message, extra={"statuscode":exc.status})
    return JSONResponse(response.dict(), status_code=exc.status)


@inject
async def handle_service_exceptions(request, exc, logger = Provide[CoreContainer.app_logger]):
    """
        handling ServiceException
    """
    response = Response(msg=exc.message, is_success=False)
    return JSONResponse(response.dict(), status_code=exc.status)


def prepare_error(obj, keys, msg) -> dict:
    def prepare_dict(obj, keys):
        if len(keys) == 0:
            return msg
        
        key = keys[0]
        if key not in obj:
            obj[key] = {}

        obj[key] = prepare_dict(obj[key], keys[1:])
        return obj

    return prepare_dict(obj, keys)


@inject
async def validation_exception_handler(request, exc, logger = Provide[CoreContainer.app_logger]):
    """
        pydantic RequestValidationError
    """
    errors = {}

    for err in exc.errors():     
        loc = err.get('loc')
        msg = err.get('msg') 
        errors = prepare_error(errors, loc[1:], msg)
    
    response = Response(msg=errors, is_success=False)
    logger.error(str(errors), extra={"statuscode": 422})
    return JSONResponse(response.dict(), status_code=422)
