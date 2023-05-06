from pydantic import BaseModel
from typing import List, Optional


class AmentyCreate(BaseModel):
    name: str
    icon: Optional[str]
    description: Optional[str]


class AmentyUpdate(BaseModel):
    name: Optional[str]
    icon: Optional[str]
    description: Optional[str]


class AmentyOut(BaseModel):
    id: int
    name: str
    icon: Optional[str]
    description: Optional[str]

    class Config:
        orm_mode = True
