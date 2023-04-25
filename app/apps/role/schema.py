from pydantic import BaseModel
from typing import List


class RoleCreate(BaseModel):
    title: str


class RoleUpdate(BaseModel):
    title: str


class RoleOut(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True
