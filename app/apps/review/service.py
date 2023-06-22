from app.core.service.base import BaseSqlAlchemyServiceWithLogging
from .repo import ReviewRepo


class ReviewService(BaseSqlAlchemyServiceWithLogging[ReviewRepo]):
    async def create_review(self, db_session, obj_in, user_id):
        obj_in={**obj_in.dict(), "user_id": user_id}
        obj = await self.repo.create(db_session, obj_in)
        await db_session.commit()

    async def get_review(self, db_session, id):
        return await self.repo.get(db_session, id)

    async def get_room_reviews(self, db_session, room_id):
        return await self.repo.get_review_by_room_id(db_session, room_id)
    
    async def update_review(self, db_session, id, obj_in):
        obj = await self.repo.update(db_session, id, obj_in)
        await db_session.commit()
        return obj

    async def delete_review(self, db_session, id):
        await self.repo.delete(db_session, id=id)
        await db_session.commit()
    