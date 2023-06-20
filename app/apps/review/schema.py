from pydantic import BaseModel
from typing import Optional


class ReviewCreate(BaseModel):
    room_id: int
    stars: int
    comment: Optional[str]


class ReviewUpdate(BaseModel):
    stars: Optional[int]
    comment: Optional[str]


class UserInReview(BaseModel):
    id: int
    full_name: str
    avatar: Optional[str]

    class Config:
        orm_mode = True

class ReviewOut(BaseModel):
    id: int
    room_id: int
    user: UserInReview
    stars: int
    comment: Optional[str]

    class Config:
        orm_mode = True
