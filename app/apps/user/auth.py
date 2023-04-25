from fastapi import Depends, Request
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.utils import get_authorization_scheme_param
from dependency_injector.wiring import inject, Provide
from typing import Annotated, Optional, List
from jose import jwt, JWTError

from app.core.config.settings import app_settings
from app.core.exceptions.http import CustomHTTPException
from app.core.database.deps import get_db
from .container import UserContainer
from .schema import TokenDataIn, UserOut


class CustomOAuth2PasswordBearer(OAuth2PasswordBearer):
    async def __call__(self, request: Request) -> Optional[str]:
        authorization = request.cookies.get("access_token")
        scheme, param = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise CustomHTTPException(message="Not authenticated", status=401)
            else:
                return None
        return param


oauth2_schema = CustomOAuth2PasswordBearer(tokenUrl=f"{app_settings.root_path[::-1]}{app_settings.PREFIX}auth/login")


@inject
async def get_current_user(
    token: Annotated[str, Depends(oauth2_schema)],
    db_session = Depends(get_db),
    user_service = Depends(Provide[UserContainer.user_service])
):
    credentials_exception = CustomHTTPException(message="Could not validate credentials", status=401)
    try:
        user_data = jwt.decode(token, app_settings.SECRET_KEY, algorithms=[app_settings.ALGORITHM,])
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