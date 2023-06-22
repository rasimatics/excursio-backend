from pydantic import BaseModel, validator
from datetime import date
from typing import Optional

from ..room.schema import ReservationRoomOut


class ReservationCreate(BaseModel):
    check_in: Optional[date]
    check_out: Optional[date]
    price: float
    room_id: int

    @validator("check_out")
    def check_date(cls, check_out, values):
        if check_out < values['check_in']:
            raise ValueError("Çıxış tarixi başlanğıc tarixdən sonra olmalıdır!")
        return check_out




class ReservationOut(BaseModel):
    id: int
    check_in: Optional[date]
    check_out: Optional[date]
    price: float
    room: ReservationRoomOut
    user_id: int

    class Config:
        orm_mode = True
