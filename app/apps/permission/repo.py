from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from typing import List

from app.core.repo.base import BaseSqlalchemyRepo
from app.core.exceptions.repo import RepoException
from .models import Permission


class PermissionRepo(BaseSqlalchemyRepo):
    model = Permission

    async def create(self, db_session, obj_in):
        """
            Create permission
        """
        try:
            return await super().create(db_session, obj_in)
        except IntegrityError as e:
            raise RepoException("Permission title must be unique", e)

    async def get(self, db_session, id):
        """
            Get permission by id
        """
        obj = await super().get(db_session, id)

        if not obj:
            raise RepoException("Permission not found", None, status=404)
        return obj
    
    async def get_many(self, db_session, ids: List[int]):
        stmt = select(self.model).where(self.model.id.in_(ids))
        result = await db_session.execute(stmt)
        return result.scalars().all()

    async def get_all(self, db_session):
        """
            Get all permissions
        """
        return await super().list(db_session)
    
    async def update(self, db_session, id, obj_in):
        """
            Update permission by id
        """
        db_obj = await self.get(db_session, id)
        
        if not db_obj:
            raise RepoException("Permission not found", None, status=404)
        
        try:
            return await super().update(db_session, db_obj, obj_in)
        except IntegrityError as e:
                raise RepoException("Permission title must be unique", e)

    async def delete(self, db_session, id):
        """
            Delete permission by id
        """
        db_obj = await self.get(db_session, id=id)
        
        if not db_obj:
            raise RepoException("Permission not found", None, status=404)
        
        return await super().delete(db_session, id=id)
