from sqlalchemy import select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import selectinload 
from datetime import datetime

from app.core.repo.base import BaseSqlalchemyRepo
from app.core.exceptions.repo import RepoException
from .models import User


class UserRepo(BaseSqlalchemyRepo):
    model = User

    async def create(self, db_session, obj_in):
        """
            Create user
        """
        try:
            return await super().create(db_session, obj_in)
        except IntegrityError as e:
            raise RepoException(e.orig.__cause__.detail, e)

    async def get(self, db_session, id):
        """
            Get user by id
        """
        stmt = select(self.model) \
                    .options(selectinload(self.model.role))\
                    .where(self.model.id == id)
        result = await db_session.execute(stmt)
        obj = result.scalars().one_or_none()

        if not obj:
            raise RepoException("User not found", None, status=404)
        return obj
    
    async def get_by_email(self, db_session, email):
        """
            Get user by username
        """
        stmt = select(self.model)\
                .options(selectinload(self.model.role))\
                .where(self.model.email == email)
        result = await db_session.execute(stmt)
        return result.scalars().one_or_none()


    async def get_all(self, db_session):
        """
            Get all users
        """
        stmt = select(self.model)\
                .options(selectinload(self.model.role))
        result = await db_session.execute(stmt)
        return result.scalars().all()
    
    async def update(self, db_session, id, obj_in):
        """
            Update user by id
        """
        db_obj = await self.get(db_session, id)
        
        if not db_obj:
            raise RepoException("User not found", None, status=404)
        
        try:
            return await super().update(db_session, db_obj, obj_in)
        except IntegrityError as e:
            raise RepoException(e.orig.__cause__.detail, e)

    async def delete(self, db_session, id):
        """
            Delete user by id
        """
        db_obj = await self.get(db_session, id=id)
        
        if not db_obj:
            raise RepoException("User not found", None, status=404)
        
        return await super().delete(db_session, id=id)
    

    async def update_after_login(self, db_session, id, last_ip: str, last_login: datetime):
        db_obj = await self.get(db_session, id=id)
        db_obj.last_ip = last_ip
        db_obj.last_login = last_login

        db_session.add(db_obj)
        await db_session.flush()