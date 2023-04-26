from fastapi import APIRouter

from app.core.config.settings import app_settings
from ..role.controller import role_router
from ..user.controller import user_router, auth_router

"""
    Include all apps routers
"""
router = APIRouter(prefix=app_settings.PREFIX)

router.include_router(role_router)
router.include_router(user_router)
router.include_router(auth_router)
