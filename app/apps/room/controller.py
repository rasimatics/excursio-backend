from fastapi import APIRouter, Depends, UploadFile
from typing import List
from dependency_injector.wiring import inject, Provide
from app.core.database.deps import get_db
from app.core.response.base import Response
from ..user.auth import get_current_user
from .schema import RoomCreate, RoomOut
from .container import RoomContainer


room_router = APIRouter(prefix="/rooms", tags=['Rooms',])


@room_router.post("/", status_code=201)
@inject
async def create_room(
    room: RoomCreate, 
    photos: List[UploadFile],
    db_session = Depends(get_db),
    room_service = Depends(Provide[RoomContainer.room_service]),
    user = Depends(get_current_user)
) -> Response:
    await room_service.create_room(db_session, room, photos, user.id)
    return {
        "msg": "Room created successfully",
        "result": None,
        "is_success": True
    }


@room_router.get("/", status_code=200)
@inject
async def get_rooms(
    db_session = Depends(get_db),
    room_service = Depends(Provide[RoomContainer.room_service])
) -> Response:
    result = await room_service.get_rooms(db_session)
    return {
        "msg": "Rooms get successfully",
        "result": result,
        "is_success": True
    }


@room_router.get("/{room_id}", status_code=200)
@inject
async def get_room(
    room_id: int,
    db_session = Depends(get_db),
    room_service = Depends(Provide[RoomContainer.room_service])
) -> Response[RoomOut]:
    result = await room_service.get_room_detail(db_session, room_id)
    return {
        "msg": "Room get successfully",
        "result": result,
        "is_success": True
    }



