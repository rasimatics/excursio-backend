from sqlalchemy.exc import IntegrityError

from app.core.repo.base import BaseSqlalchemyRepo
from app.core.exceptions.repo import RepoException
from .models import Amenty


class AmentyRepo(BaseSqlalchemyRepo):
    model = Amenty

    async def create(self, db_session, obj_in):
        """
            Create amenty
        """
        try:
            return await super().create(db_session, obj_in)
        except IntegrityError as e:
            raise RepoException("Amenty name must be unique", e)

    async def get(self, db_session, id):
        """
            Get amenty by id
        """
        obj = await super().get(db_session, id)

        if not obj:
            raise RepoException("Amenty not found", None, status=404)
        return obj

    async def get_all(self, db_session):
        """
            Get all amentys
        """
        return await super().list(db_session)
    
    async def update(self, db_session, id, obj_in):
        """
            Update amenty by id
        """
        db_obj = await self.get(db_session, id)
        
        if not db_obj:
            raise RepoException("Amenty not found", None, status=404)
        
        try:
            return await super().update(db_session, db_obj, obj_in)
        except IntegrityError as e:
                raise RepoException("Amenty title must be unique", e)

    async def delete(self, db_session, id):
        """
            Delete amenty by id
        """
        db_obj = await self.get(db_session, id=id)
        
        if not db_obj:
            raise RepoException("Amenty not found", None, status=404)
        
        return await super().delete(db_session, id=id)
