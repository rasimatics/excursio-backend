from fastapi import APIRouter, Depends
from typing import List
from dependency_injector.wiring import inject, Provide
from app.core.database.deps import get_db
from app.core.response.base import Response
from .schema import PermissionCreate, PermissionUpdate, PermissionOut
from .container import PermissionContainer


permission_router = APIRouter(prefix="/permissions", tags=['Permissions',])


@permission_router.post("/", status_code=201)
@inject
async def create_permission(
    obj_in: PermissionCreate,
    db_session = Depends(get_db),
    perm_service = Depends(Provide[PermissionContainer.permission_service])
) -> Response[PermissionOut]:
    result = await perm_service.create_permission(db_session, obj_in)
    return {
        "msg": "Permission created successfully",
        "result": result,
        "is_success": True
    }


@permission_router.get("/")
@inject
async def get_all_permissions(
    db_session = Depends(get_db),
    perm_service = Depends(Provide[PermissionContainer.permission_service])
) -> Response[List[PermissionOut]]:
    result = await perm_service.get_all_permissions(db_session)
    return {
        "msg": "Permission list successfully",
        "result": result,
        "is_success": True
    }


@permission_router.get("/{id}")
@inject
async def get_permission(
    id: int,
    db_session = Depends(get_db),
    perm_service = Depends(Provide[PermissionContainer.permission_service])
) -> Response[PermissionOut]:
    result = await perm_service.get_permission(db_session, id=id)
    return {
            "msg": "Permission get successfully",
            "result": result,
            "is_success": True
        }
    

@permission_router.put("/{id}")
@inject
async def update_permission(
    id: int,
    obj_in: PermissionUpdate,
    db_session = Depends(get_db),
    perm_service = Depends(Provide[PermissionContainer.permission_service])
) -> Response[PermissionOut]:
    result = await perm_service.update_permission(db_session, id, obj_in)
    return {
        "msg": "Permission updated successfully",
        "result": result,
        "is_success": True
    }


@permission_router.delete("/{id}")
@inject
async def delete_permission(
    id: int,
    db_session = Depends(get_db),
    perm_service = Depends(Provide[PermissionContainer.permission_service])
) -> Response:
    await perm_service.delete_permission(db_session, id=id)
    return {
        "msg": "Permission deleted successfully",
        "result": None,
        "is_success": True
    }
