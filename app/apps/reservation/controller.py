from fastapi import APIRouter, Depends
from typing import List
from dependency_injector.wiring import inject, Provide
from app.core.database.deps import get_db
from app.core.response.base import Response
from ..user.auth import get_current_user
from .schema import ReservationCreate, ReservationOut
from .container import ReservationContainer


reservation_router = APIRouter(prefix="/reservations", tags=['Reservations',])

@reservation_router.post("/", status_code=201)
@inject
async def create_reservation(
    obj_in: ReservationCreate,
    db_session = Depends(get_db),
    reservation_service = Depends(Provide[ReservationContainer.reservation_service]),
    user = Depends(get_current_user)
) -> Response:
    result = await reservation_service.create_reservation(db_session, obj_in, user.id)
    return {
        "msg": "Reservation created successfully",
        "result": result,
        "is_success": True
    }


@reservation_router.get("/")
@inject
async def get_all_reservations(
    db_session = Depends(get_db),
    reservation_service = Depends(Provide[ReservationContainer.reservation_service]),
    user = Depends(get_current_user)
) -> Response[List[ReservationOut]]:
    result = await reservation_service.get_user_reservations(db_session, user.id)
    return {
        "msg": "Reservation list successfully",
        "result": result,
        "is_success": True
    }
