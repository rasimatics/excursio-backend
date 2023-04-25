from fastapi import APIRouter, Depends
from typing import List
from dependency_injector.wiring import inject, Provide
from app.core.database.deps import get_db
from app.core.response.base import Response
from .schema import RoleCreate, RoleUpdate, RoleOut
from .container import RoleContainer


role_router = APIRouter(prefix="/roles", tags=['Roles',])


@role_router.post("/", status_code=201)
@inject
async def create_role(
    obj_in: RoleCreate,
    db_session = Depends(get_db),
    role_service = Depends(Provide[RoleContainer.role_service])
) -> Response[RoleOut]:
    result = await role_service.create_role(db_session, obj_in)
    return {
        "msg": "Role created successfully",
        "result": result,
        "is_success": True
    }


@role_router.get("/")
@inject
async def get_all_roles(
    db_session = Depends(get_db),
    role_service = Depends(Provide[RoleContainer.role_service])
) -> Response[List[RoleOut]]:
    result = await role_service.get_all_roles(db_session)
    return {
        "msg": "Role list successfully",
        "result": result,
        "is_success": True
    }


@role_router.get("/{id}")
@inject
async def get_role(
    id: int,
    db_session = Depends(get_db),
    role_service = Depends(Provide[RoleContainer.role_service])
) -> Response[RoleOut]:
    result = await role_service.get_role(db_session, id=id)
    return {
            "msg": "Role get successfully",
            "result": result,
            "is_success": True
        }
    

@role_router.put("/{id}")
@inject
async def update_role(
    id: int,
    obj_in: RoleUpdate,
    db_session = Depends(get_db),
    role_service = Depends(Provide[RoleContainer.role_service])
) -> Response[RoleOut]:
    result = await role_service.update_role(db_session, id, obj_in)
    return {
        "msg": "Role updated successfully",
        "result": result,
        "is_success": True
    }


@role_router.delete("/{id}")
@inject
async def delete_role(
    id: int,
    db_session = Depends(get_db),
    role_service = Depends(Provide[RoleContainer.role_service])
) -> Response:
    await role_service.delete_role(db_session, id=id)
    return {
        "msg": "Role deleted successfully",
        "result": None,
        "is_success": True
    }
