from pydantic import BaseModel
from datetime import date, datetime


class ReservationCreate(BaseModel):
    check_in: date
    check_out: date
    price: float
    room_id: int


class ReservationOut(BaseModel):
    id: int
    check_in: date
    check_out: date
    price: float
    room_id: int
    user_id: int

    class Config:
        orm_mode = True
