from fastapi import APIRouter, Depends
from typing import List
from dependency_injector.wiring import inject, Provide
from app.core.database.deps import get_db
from app.core.response.base import Response
from .schema import AmentyCreate, AmentyUpdate, AmentyOut
from .container import AmentyContainer


amenty_router = APIRouter(prefix="/amenties", tags=['Amenty',])


@amenty_router.post("/", status_code=201)
@inject
async def create_amenty(
    obj_in: AmentyCreate,
    db_session = Depends(get_db),
    amenty_service = Depends(Provide[AmentyContainer.amenty_service])
) -> Response[AmentyOut]:
    result = await amenty_service.create_amenty(db_session, obj_in)
    return {
        "msg": "Amenty created successfully",
        "result": result,
        "is_success": True
    }


@amenty_router.get("/")
@inject
async def get_all_amentys(
    db_session = Depends(get_db),
    amenty_service = Depends(Provide[AmentyContainer.amenty_service])
) -> Response[List[AmentyOut]]:
    result = await amenty_service.get_all_amentys(db_session)
    return {
        "msg": "Amenty list successfully",
        "result": result,
        "is_success": True
    }


@amenty_router.get("/{id}")
@inject
async def get_amenty(
    id: int,
    db_session = Depends(get_db),
    amenty_service = Depends(Provide[AmentyContainer.amenty_service])
) -> Response[AmentyOut]:
    result = await amenty_service.get_amenty(db_session, id=id)
    return {
            "msg": "Amenty get successfully",
            "result": result,
            "is_success": True
        }
    

@amenty_router.put("/{id}")
@inject
async def update_amenty(
    id: int,
    obj_in: AmentyUpdate,
    db_session = Depends(get_db),
    amenty_service = Depends(Provide[AmentyContainer.amenty_service])
) -> Response[AmentyOut]:
    result = await amenty_service.update_amenty(db_session, id, obj_in)
    return {
        "msg": "Amenty updated successfully",
        "result": result,
        "is_success": True
    }


@amenty_router.delete("/{id}")
@inject
async def delete_amenty(
    id: int,
    db_session = Depends(get_db),
    amenty_service = Depends(Provide[AmentyContainer.amenty_service])
) -> Response:
    await amenty_service.delete_amenty(db_session, id=id)
    return {
        "msg": "Amenty deleted successfully",
        "result": None,
        "is_success": True
    }
