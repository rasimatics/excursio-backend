from pydantic import BaseModel
from typing import List, Optional


class CategoryCreate(BaseModel):
    name: str
    icon: Optional[str]
    description: Optional[str]


class CategoryUpdate(BaseModel):
    name: Optional[str]
    icon: Optional[str]
    description: Optional[str]


class CategoryOut(BaseModel):
    id: int
    name: str
    icon: Optional[str]
    description: Optional[str]

    class Config:
        orm_mode = True
