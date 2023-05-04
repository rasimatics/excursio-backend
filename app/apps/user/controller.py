from fastapi import APIRouter, Depends, Response as FastAPIResponse, Request
from typing import List
from dependency_injector.wiring import inject, Provide
from app.core.database.deps import get_db
from app.core.response.base import Response
from .auth import get_current_user, check_role, check_permissions
from .schema import UserCreate, UserUpdate, UserOut, UserLogin, TokenDataOut, TokenOut
from .container import UserContainer
from .security import create_access_token
from .service import UserService


user_router = APIRouter(prefix="/users", tags=['Users',])
auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post("/login")
@inject
async def login(
    user_data: UserLogin,
    response: FastAPIResponse,
    db_session = Depends(get_db),
    user_service = Depends(Provide[UserContainer.user_service])
) -> Response[TokenOut]:
    
    user: UserOut = await user_service.authenticate_user(db_session, user_data.email, user_data.password)
    token_data = TokenDataOut(**{**user.dict(), "role": user.get_role()})
    access_token = create_access_token(data=token_data.dict())
    result = TokenOut(access_token=access_token, token_type="bearer")
    return {
        "msg": "User logged in successfully",
        "result": result,
        "is_success": True
    } 


@auth_router.post("/logout")
@inject
async def logout(
    response: FastAPIResponse,
) -> Response:
    response.delete_cookie("access_token")
    return {
        "msg": "User logged out successfully",
        "result": None,
        "is_success": True
    } 


@user_router.get("/me", status_code=201)
@inject
async def get_current_user(
    db_session = Depends(get_db),
    user_service: UserService = Depends(Provide[UserContainer.user_service]),
    user = Depends(get_current_user)
) -> Response[UserOut]:
    result = await user_service.get_user(db_session, user.id)
    return {
        "msg": "User get successfully",
        "result": result,
        "is_success": True
    }



@user_router.post("/", status_code=201)
@inject
async def create_user(
    obj_in: UserCreate,
    db_session = Depends(get_db),
    user_service = Depends(Provide[UserContainer.user_service])
) -> Response[UserOut]:
    result = await user_service.create_user(db_session, obj_in)
    return {
        "msg": "User created successfully",
        "result": result,
        "is_success": True
    }


@user_router.get("/")
@inject
async def get_all_users(
    db_session = Depends(get_db),
    user_service = Depends(Provide[UserContainer.user_service]),
) -> Response[List[UserOut]]:
    result = await user_service.get_all_users(db_session)
    return {
        "msg": "User list successfully",
        "result": result,
        "is_success": True
    }


@user_router.get("/{id}")
@inject
async def get_user(
    id: int,
    db_session = Depends(get_db),
    user_service = Depends(Provide[UserContainer.user_service])
) -> Response[UserOut]:
    result = await user_service.get_user(db_session, id=id)
    return {
            "msg": "User get successfully",
            "result": result,
            "is_success": True
        }
    

@user_router.put("/{id}")
@inject
async def update_user(
    id: int,
    obj_in: UserUpdate,
    db_session = Depends(get_db),
    user_service: UserService = Depends(Provide[UserContainer.user_service]),
    user: UserOut = Depends(get_current_user)
) -> Response[UserOut]:
    result = await user_service.update_user(db_session, user, id, obj_in)
    return {
        "msg": "User updated successfully",
        "result": result,
        "is_success": True
    }


@user_router.delete("/{id}")
@inject
async def delete_user(
    id: int,
    db_session = Depends(get_db),
    user_service = Depends(Provide[UserContainer.user_service])
) -> Response:
    await user_service.delete_user(db_session, id=id)
    return {
        "msg": "User deleted successfully",
        "result": None,
        "is_success": True
    }