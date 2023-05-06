from fastapi import APIRouter, Depends
from typing import List
from dependency_injector.wiring import inject, Provide
from app.core.database.deps import get_db
from app.core.response.base import Response
from .schema import CategoryCreate, CategoryUpdate, CategoryOut
from .container import CategoryContainer


category_router = APIRouter(prefix="/categories", tags=['Category',])


@category_router.post("/", status_code=201)
@inject
async def create_category(
    obj_in: CategoryCreate,
    db_session = Depends(get_db),
    category_service = Depends(Provide[CategoryContainer.category_service])
) -> Response[CategoryOut]:
    result = await category_service.create_category(db_session, obj_in)
    return {
        "msg": "Category created successfully",
        "result": result,
        "is_success": True
    }


@category_router.get("/")
@inject
async def get_all_categorys(
    db_session = Depends(get_db),
    category_service = Depends(Provide[CategoryContainer.category_service])
) -> Response[List[CategoryOut]]:
    result = await category_service.get_all_categorys(db_session)
    return {
        "msg": "Category list successfully",
        "result": result,
        "is_success": True
    }


@category_router.get("/{id}")
@inject
async def get_category(
    id: int,
    db_session = Depends(get_db),
    category_service = Depends(Provide[CategoryContainer.category_service])
) -> Response[CategoryOut]:
    result = await category_service.get_category(db_session, id=id)
    return {
            "msg": "Category get successfully",
            "result": result,
            "is_success": True
        }
    

@category_router.put("/{id}")
@inject
async def update_category(
    id: int,
    obj_in: CategoryUpdate,
    db_session = Depends(get_db),
    category_service = Depends(Provide[CategoryContainer.category_service])
) -> Response[CategoryOut]:
    result = await category_service.update_category(db_session, id, obj_in)
    return {
        "msg": "Category updated successfully",
        "result": result,
        "is_success": True
    }


@category_router.delete("/{id}")
@inject
async def delete_category(
    id: int,
    db_session = Depends(get_db),
    category_service = Depends(Provide[CategoryContainer.category_service])
) -> Response:
    await category_service.delete_category(db_session, id=id)
    return {
        "msg": "Category deleted successfully",
        "result": None,
        "is_success": True
    }
