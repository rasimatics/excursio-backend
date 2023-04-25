from pydantic import BaseModel
from typing import List


class PermissionCreate(BaseModel):
    title: str


class PermissionUpdate(BaseModel):
    title: str


class PermissionOut(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True