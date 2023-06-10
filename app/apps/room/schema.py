import json
from pydantic import BaseModel
from typing import List
from ..user.schema import UserRoomOut
from ..category.schema import CategoryOut
from ..amenty.schema import AmentyOut


class RoomAmenityDb(BaseModel):
    amenity_id: int
    room_id: int


class PhotoCreate(BaseModel):
    url: str


class PhotoDb(BaseModel):
    url: str
    room_id: int


class PhotoOut(BaseModel):
    id: int
    url: str

    class Config:
        orm_mode = True


class RoomCreate(BaseModel):
    price: float
    room_count: float
    bed_count: float
    max_guest_count: float
    title: str
    description: str
    longitude: float
    latitude: float
    address_state: str
    address_city: str
    address_city: str
    address_zip_code: str
    room_type: int
    amenities: List[int]

    @classmethod
    def validate(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return super().validate(value)


class RoomOut(BaseModel):
    id: int
    price: float
    room_count: float
    bed_count: float
    max_guest_count: float
    title: str
    description: str
    longitude: float
    latitude: float
    address_state: str
    address_city: str
    address_city: str
    address_zip_code: str
    category: CategoryOut
    host: UserRoomOut
    photos: List[PhotoOut]
    amenities: List[AmentyOut]

    class Config:
        orm_mode = True


class ReservationRoomOut(BaseModel):
    id: int
    price: float
    title: str
    description: str
    photos: List[PhotoOut]

    class Config:
        orm_mode = True