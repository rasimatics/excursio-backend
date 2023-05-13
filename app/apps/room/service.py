from logging import Logger
from sqlalchemy.orm import Session
from app.core.service.base import BaseService
from app.core.exceptions.service import ServiceException
from .repo import RoomAmenitiesRepo, RoomRepo, PhotoRepo
from .schema import RoomCreate, PhotoDb, RoomAmenityDb
from .utils import create_filename, save_file


class RoomService(BaseService):
    def __init__(self, room_repo: RoomRepo, amenity_repo: RoomAmenitiesRepo, photo_repo: PhotoRepo, logger: Logger) -> None:
        self.room_repo = room_repo
        self.amenity_repo = amenity_repo
        self.photo_repo = photo_repo
        self.logger = logger

    async def create_room(self, db_session: Session, room_in: RoomCreate, photos_in):
        amenities_in = room_in.amenities
        try:
            room = await self.room_repo.create(session=db_session, obj_in=room_in.dict(exclude={"amenities", "photos"}))

            for photo in photos_in:
                photo.filename = create_filename(photo.filename)
                url = save_file(photo)
                photo_db = PhotoDb(url=url, room_id=room.id)
                await self.photo_repo.create(session=db_session, obj_in=photo_db.dict())    

            for amenity_id in amenities_in:
                amenity_db = RoomAmenityDb(amenity_id=amenity_id, room_id=room.id)
                await self.amenity_repo.create(db_session, amenity_db)   

            await db_session.commit()
        except Exception as e:
            await db_session.rollback()
            raise ServiceException(str(e))
        
    async def get_room_detail(self, db_session, id: int):
        return await self.room_repo.get(db_session, id=id)
    
    async def get_rooms(self, db_session: Session):
        return await self.room_repo.list(db_session)

        