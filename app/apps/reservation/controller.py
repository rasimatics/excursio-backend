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


@reservation_router.get("/", response_model=Response[List[ReservationOut]])
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


@reservation_router.delete("/{reservation_id}", response_model=Response[List[ReservationOut]])
@inject
async def cancel_reservation(
    reservation_id: int,
    db_session = Depends(get_db),
    reservation_service = Depends(Provide[ReservationContainer.reservation_service]),
    user = Depends(get_current_user)
) -> Response[List[ReservationOut]]:
    result = await reservation_service.cancel_reservation(db_session, reservation_id, user.id)
    return {
        "msg": "Reservation canceled successfully",
        "result": result,
        "is_success": True
    }