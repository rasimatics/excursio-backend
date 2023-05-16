from app.core.service.base import BaseSqlAlchemyServiceWithLogging
from .repo import ReservationRepo


class ReservationService(BaseSqlAlchemyServiceWithLogging[ReservationRepo]):
    async def create_reservation(self, db_session, obj_in, user_id):
        obj = await self.repo.create(db_session, obj_in={**obj_in.dict(), "user_id": user_id})
        await db_session.commit()
        return obj

    async def get_reservation(self, db_session, id):
        return await self.repo.get(db_session, id)

    async def get_user_reservations(self, db_session, user_id):
        return await self.repo.get_reservations_by_user_id(db_session, user_id)
    
    async def update_reservation(self, db_session, id, obj_in):
        obj = await self.repo.update(db_session, id, obj_in)
        await db_session.commit()
        return obj

    async def delete_reservation(self, db_session, id):
        await self.repo.delete(db_session, id=id)
        await db_session.commit()
    