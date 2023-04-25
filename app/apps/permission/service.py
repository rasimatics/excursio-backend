from typing import List
from sqlalchemy import select

from app.core.service.base import BaseSqlAlchemyServiceWithLogging
from .repo import PermissionRepo


class PermissionService(BaseSqlAlchemyServiceWithLogging[PermissionRepo]):
    async def create_permission(self, db_session, obj_in):
        obj = await self.repo.create(db_session, obj_in)
        await db_session.commit()
        return obj

    async def get_permission(self, db_session, id):
        return await self.repo.get(db_session, id)
    
    async def get_permissions(self, db_session, ids: List[int]):
        return await self.repo.get_many(db_session, ids)

    async def get_all_permissions(self, db_session):
        return await self.repo.get_all(db_session)
    
    async def update_permission(self, db_session, id, obj_in):
        obj = await self.repo.update(db_session, id, obj_in)
        await db_session.commit()
        return obj

    async def delete_permission(self, db_session, id):
        await self.repo.delete(db_session, id=id)
        await db_session.commit()
    