from app.core.service.base import BaseSqlAlchemyServiceWithLogging
from .repo import RoomDetailRepo


class RoomDetailService(BaseSqlAlchemyServiceWithLogging[RoomDetailRepo]):
    async def create_room_detail(self, db_session, obj_in):
        obj = await self.repo.create(db_session, obj_in)
        await db_session.commit()
        return obj

    async def get_room_detail(self, db_session, id):
        return await self.repo.get(db_session, id)

    async def get_all_room_details(self, db_session):
        return await self.repo.get_all(db_session)
    
    async def update_room_detail(self, db_session, id, obj_in):
        obj = await self.repo.update(db_session, id, obj_in)
        await db_session.commit()
        return obj

    async def delete_room_detail(self, db_session, id):
        await self.repo.delete(db_session, id=id)
        await db_session.commit()
    