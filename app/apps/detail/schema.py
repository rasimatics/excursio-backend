from pydantic import BaseModel
from typing import List, Optional


class RoomDetailCreate(BaseModel):
    name: str
    icon: str
    description: Optional[str]


class RoomDetailUpdate(BaseModel):
    icon: Optional[str]
    name: Optional[str]
    description: Optional[str]


class RoomDetailOut(BaseModel):
    id: int
    name: str
    icon: Optional[str]
    description: Optional[str]

    class Config:
        orm_mode = True
