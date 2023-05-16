from fastapi import APIRouter, Depends
from typing import List
from dependency_injector.wiring import inject, Provide
from app.core.database.deps import get_db
from app.core.response.base import Response
from ..user.auth import get_current_user
from .schema import ReviewCreate, ReviewUpdate, ReviewOut
from .container import ReviewContainer


review_router = APIRouter(prefix="/reviews", tags=['Reviews',])


@review_router.post("/", status_code=201)
@inject
async def create_review(
    obj_in: ReviewCreate,
    db_session = Depends(get_db),
    review_service = Depends(Provide[ReviewContainer.review_service]),
    user = Depends(get_current_user)
) -> Response[ReviewOut]:
    result = await review_service.create_review(db_session, obj_in, user.id)
    return {
        "msg": "Review created successfully",
        "result": result,
        "is_success": True
    }


@review_router.get("/{room_id}")
@inject
async def get_room_reviews(
    room_id: int,
    db_session = Depends(get_db),
    review_service = Depends(Provide[ReviewContainer.review_service])
) -> Response[List[ReviewOut]]:
    result = await review_service.get_room_reviews(db_session, room_id)
    return {
        "msg": "Review list successfully",
        "result": result,
        "is_success": True
    }


@review_router.put("/{id}")
@inject
async def update_review(
    id: int,
    obj_in: ReviewUpdate,
    db_session = Depends(get_db),
    review_service = Depends(Provide[ReviewContainer.review_service]),
    user = Depends(get_current_user)
) -> Response[ReviewOut]:
    result = await review_service.update_review(db_session, id, obj_in)
    return {
        "msg": "Review updated successfully",
        "result": result,
        "is_success": True
    }


@review_router.delete("/{id}")
@inject
async def delete_review(
    id: int,
    db_session = Depends(get_db),
    review_service = Depends(Provide[ReviewContainer.review_service]),
    user = Depends(get_current_user)
) -> Response:
    await review_service.delete_review(db_session, id=id)
    return {
        "msg": "Review deleted successfully",
        "result": None,
        "is_success": True
    }
