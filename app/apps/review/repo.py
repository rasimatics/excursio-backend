from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from app.core.repo.base import BaseSqlalchemyRepo
from app.core.exceptions.repo import RepoException
from .models import Review


class ReviewRepo(BaseSqlalchemyRepo):
    model = Review

    async def create(self, db_session, obj_in):
        """
            Create review
        """
        try:
            return await super().create(db_session, obj_in)
        except IntegrityError as e:
            raise RepoException("Review name must be unique", e)
        
    async def get_review_by_room_id(self, db_session, room_id):
        stmt = select(self.model).where(self.model.room_id == room_id)
        result = await db_session.execute(stmt)
        return result.scalars().all()

    async def get(self, db_session, id):
        """
            Get review by id
        """
        obj = await super().get(db_session, id)

        if not obj:
            raise RepoException("Review not found", None, status=404)
        return obj

    async def get_all(self, db_session):
        """
            Get all reviews
        """
        return await super().list(db_session)
    
    async def update(self, db_session, id, obj_in):
        """
            Update review by id
        """
        db_obj = await self.get(db_session, id)
        
        if not db_obj:
            raise RepoException("Review not found", None, status=404)
        
        try:
            return await super().update(db_session, db_obj, obj_in)
        except IntegrityError as e:
                raise RepoException("Review title must be unique", e)

    async def delete(self, db_session, id, user_id):
        """
            Delete review by id
        """
        await self.get(db_session, id=id) 
        return await super().delete(db_session, id=id)
