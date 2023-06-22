from sqlalchemy import select, func, and_
from sqlalchemy.orm import selectinload, contains_eager
from app.core.repo.base import BaseSqlalchemyRepo
from app.core.exceptions.repo import RepoException
from .models import Room, RoomAmenities, Photo


class PhotoRepo(BaseSqlalchemyRepo):
    model = Photo


class RoomAmenitiesRepo(BaseSqlalchemyRepo):
    model = RoomAmenities


class RoomRepo(BaseSqlalchemyRepo):
    model = Room

    async def get(self, session, id: int):
         return await super().get(session, id)

    async def get(self, session, id: int):
            stmt = select(self.model)\
                        .options(selectinload(self.model.host))\
                        .options(selectinload(self.model.category))\
                        .options(selectinload(self.model.photos))\
                        .options(selectinload(self.model.amenities))\
                        .options(selectinload(self.model.reservations))\
                        .where(self.model.id == id)
            result = await session.execute(stmt)
            obj = result.scalars().one_or_none()
            if not obj:
                 raise RepoException("Room not found")
            
            return obj

    async def list(self, session):
        subq = (
            select(
                func.min(Photo.id).label('photo_id'),
                Photo.room_id
            )
            .group_by(Photo.room_id)
        ).subquery()
        
        stmt = select(self.model)\
                    .options(contains_eager(Room.photos))\
                    .join(subq, and_(self.model.id == subq.c.room_id))\
                    .join(Photo, and_(subq.c.photo_id == Photo.id))
        result = await session.execute(stmt)
        return result.unique().scalars().all()
