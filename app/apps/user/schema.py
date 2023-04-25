from pydantic import BaseModel, EmailStr, validator
from typing import List
from datetime import datetime
from ..permission.schema import PermissionOut
from ..role.schema import RoleOut
from .security import hash_password


class UserCreate(BaseModel):
    company_code: int
    user_id: str
    email: EmailStr
    full_name: str
    role_id: int
    password: str
    permissions: List[int]

    @validator("password", pre=True)
    def set_password(cls, value):
        return hash_password(value)


class UserUpdate(BaseModel):
    # user can change
    dep_name: str | None
    position: str | None
    full_name: str | None
    password: str | None

    # only admin can change
    company_code: int | None
    user_id: str | None
    email: EmailStr | None
    role_id: int | None
    permissions: List[int] | None
    is_active: bool | None

    @validator("password", pre=True)
    def set_password(cls, value):
        return hash_password(value) if value else None


class UserOut(BaseModel):
    id: int
    company_code: int
    user_id: str
    email: EmailStr
    full_name: str
    is_active: bool
    dep_name: str | None
    position: str | None
    last_login: datetime | None
    last_ip: str | None
    role: RoleOut
    permissions: List[PermissionOut]

    def get_permissions(self):
        return [perm.title for perm in self.permissions]
    
    def get_role(self):
        return self.role.title

    class Config:
        orm_mode = True


class TokenDataIn(BaseModel):
    id: int
    user_id: str
    role: str
    permissions: List[str]


class TokenDataOut(BaseModel):
    id: int
    user_id: str
    role: str
    permissions: List[str]


class TokenOut(BaseModel):
    access_token: str
    token_type: str


class UserLogin(BaseModel):
    username: str
    password: str