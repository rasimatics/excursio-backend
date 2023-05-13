from pydantic import BaseModel, EmailStr, validator
from datetime import datetime
from ..role.schema import RoleOut
from .security import hash_password


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    bio: str
    role_id: int

    @validator("password", pre=True)
    def set_password(cls, value):
        return hash_password(value)


class UserUpdate(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    bio: str
    role_id: int

    @validator("password", pre=True)
    def set_password(cls, value):
        return hash_password(value) if value else None


class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    bio: str
    role: RoleOut

    def get_role(self):
        return self.role.title

    class Config:
        orm_mode = True


class UserRoomOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    bio: str

    class Config:
        orm_mode = True


class TokenDataIn(BaseModel):
    id: int
    email: EmailStr
    role: str


class TokenDataOut(BaseModel):
    id: int
    email: str
    role: str


class TokenOut(BaseModel):
    access_token: str
    token_type: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str