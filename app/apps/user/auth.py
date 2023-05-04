from fastapi import Depends, Request
from fastapi.security import HTTPBearer
from dependency_injector.wiring import inject, Provide
from typing import Annotated, Optional, List
from jose import jwt, JWTError

from app.core.config.settings import app_settings
from app.core.exceptions.http import CustomHTTPException
from app.core.database.deps import get_db
from .container import UserContainer
from .schema import TokenDataIn, UserOut

oauth2_schema = HTTPBearer()


@inject
async def get_current_user(
    schema: Annotated[str, Depends(oauth2_schema)],
    db_session = Depends(get_db),
    user_service = Depends(Provide[UserContainer.user_service])
):
    credentials_exception = CustomHTTPException(message="Could not validate credentials", status=401)
    try:
        user_data = jwt.decode(schema.credentials, app_settings.SECRET_KEY, algorithms=[app_settings.ALGORITHM,])
        token_data = TokenDataIn(**user_data)
    except JWTError:
        raise credentials_exception

    return await user_service.get_user(db_session, id = token_data.id)


def check_permissions(required_permissions: List[str]):
    def check(user: UserOut = Depends(get_current_user)):        
        if all(perm in user.get_permissions() for perm in required_permissions):
            return user
        raise CustomHTTPException(message="Insufficent permissions", status=403)

    return check


def check_role(permitted_roles: List[str]):
    def check(user: UserOut = Depends(get_current_user)):
        if any(role == user.get_role() for role in permitted_roles):
            return user
        raise CustomHTTPException(message="Insufficent permissions", status=403)

    return check