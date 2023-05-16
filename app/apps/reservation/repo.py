from sqlalchemy.exc import IntegrityError
from sqlalchemy import select

from app.core.repo.base import BaseSqlalchemyRepo
from app.core.exceptions.repo import RepoException
from .models import Reservation


class ReservationRepo(BaseSqlalchemyRepo):
    model = Reservation

    async def create(self, db_session, obj_in):
        """
            Create reservation
        """
        try:
            return await super().create(db_session, obj_in)
        except IntegrityError as e:
            raise RepoException("Reservation name must be unique", e)

    async def get(self, db_session, id):
        """
            Get reservation by id
        """
        obj = await super().get(db_session, id)

        if not obj:
            raise RepoException("Reservation not found", None, status=404)
        return obj
    
    async def get_reservations_by_user_id(self, db_session, user_id):
        stmt = select(self.model).where(self.model.user_id == user_id)
        result = await db_session.execute(stmt)
        return result.scalars().all()

    async def get_all(self, db_session):
        """
            Get all reservations
        """
        return await super().list(db_session)
    
    async def update(self, db_session, id, obj_in):
        """
            Update reservation by id
        """
        db_obj = await self.get(db_session, id)
        
        if not db_obj:
            raise RepoException("Reservation not found", None, status=404)
        
        try:
            return await super().update(db_session, db_obj, obj_in)
        except IntegrityError as e:
                raise RepoException("Reservation title must be unique", e)

    async def delete(self, db_session, id):
        """
            Delete reservation by id
        """
        db_obj = await self.get(db_session, id=id)
        
        if not db_obj:
            raise RepoException("Reservation not found", None, status=404)
        
        return await super().delete(db_session, id=id)
