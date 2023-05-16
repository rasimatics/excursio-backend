# from fastapi import APIRouter, Depends
# from typing import List
# from dependency_injector.wiring import inject, Provide
# from app.core.database.deps import get_db
# from app.core.response.base import Response
# from .schema import RoomDetailCreate, RoomDetailUpdate, RoomDetailOut
# from .container import RoomDetailContainer


# room_detail_router = APIRouter(prefix="/room-detail", tags=['Room Detail',])


# @room_detail_router.post("/", status_code=201)
# @inject
# async def create_room_detail(
#     obj_in: RoomDetailCreate,
#     db_session = Depends(get_db),
#     room_detail_service = Depends(Provide[RoomDetailContainer.room_detail_service])
# ) -> Response[RoomDetailOut]:
#     result = await room_detail_service.create_room_detail(db_session, obj_in)
#     return {
#         "msg": "RoomDetail created successfully",
#         "result": result,
#         "is_success": True
#     }


# @room_detail_router.get("/")
# @inject
# async def get_all_room_details(
#     db_session = Depends(get_db),
#     room_detail_service = Depends(Provide[RoomDetailContainer.room_detail_service])
# ) -> Response[List[RoomDetailOut]]:
#     result = await room_detail_service.get_all_room_details(db_session)
#     return {
#         "msg": "RoomDetail list successfully",
#         "result": result,
#         "is_success": True
#     }


# @room_detail_router.get("/{id}")
# @inject
# async def get_room_detail(
#     id: int,
#     db_session = Depends(get_db),
#     room_detail_service = Depends(Provide[RoomDetailContainer.room_detail_service])
# ) -> Response[RoomDetailOut]:
#     result = await room_detail_service.get_room_detail(db_session, id=id)
#     return {
#             "msg": "RoomDetail get successfully",
#             "result": result,
#             "is_success": True
#         }
    

# @room_detail_router.put("/{id}")
# @inject
# async def update_room_detail(
#     id: int,
#     obj_in: RoomDetailUpdate,
#     db_session = Depends(get_db),
#     room_detail_service = Depends(Provide[RoomDetailContainer.room_detail_service])
# ) -> Response[RoomDetailOut]:
#     result = await room_detail_service.update_room_detail(db_session, id, obj_in)
#     return {
#         "msg": "RoomDetail updated successfully",
#         "result": result,
#         "is_success": True
#     }


# @room_detail_router.delete("/{id}")
# @inject
# async def delete_room_detail(
#     id: int,
#     db_session = Depends(get_db),
#     room_detail_service = Depends(Provide[RoomDetailContainer.room_detail_service])
# ) -> Response:
#     await room_detail_service.delete_room_detail(db_session, id=id)
#     return {
#         "msg": "RoomDetail deleted successfully",
#         "result": None,
#         "is_success": True
#     }
