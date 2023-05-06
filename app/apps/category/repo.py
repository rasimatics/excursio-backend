from sqlalchemy.exc import IntegrityError

from app.core.repo.base import BaseSqlalchemyRepo
from app.core.exceptions.repo import RepoException
from .models import Category


class CategoryRepo(BaseSqlalchemyRepo):
    model = Category

    async def create(self, db_session, obj_in):
        """
            Create category
        """
        try:
            return await super().create(db_session, obj_in)
        except IntegrityError as e:
            raise RepoException("Category name must be unique", e)

    async def get(self, db_session, id):
        """
            Get category by id
        """
        obj = await super().get(db_session, id)

        if not obj:
            raise RepoException("Category not found", None, status=404)
        return obj

    async def get_all(self, db_session):
        """
            Get all categorys
        """
        return await super().list(db_session)
    
    async def update(self, db_session, id, obj_in):
        """
            Update category by id
        """
        db_obj = await self.get(db_session, id)
        
        if not db_obj:
            raise RepoException("Category not found", None, status=404)
        
        try:
            return await super().update(db_session, db_obj, obj_in)
        except IntegrityError as e:
                raise RepoException("Category title must be unique", e)

    async def delete(self, db_session, id):
        """
            Delete category by id
        """
        db_obj = await self.get(db_session, id=id)
        
        if not db_obj:
            raise RepoException("Category not found", None, status=404)
        
        return await super().delete(db_session, id=id)
