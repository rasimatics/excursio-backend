from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from app.core.database.base import Base


class Room(Base):
    id = Column(Integer, primary_key=True, index=True)
    price = Column(Float)
    room_count = Column(Integer)
    bed_count = Column(Integer)
    max_guest_count = Column(Integer)
    title = Column(String(length=100))
    description = Column(Text)
    longitude = Column(Float)
    latitude = Column(Float)
    address_state = Column(Text)
    address_city = Column(Text)
    address_street = Column(Text)
    address_zip_code = Column(String(length=50))

    room_type = Column(ForeignKey("category.id"), nullable=False)
    host_id = Column(ForeignKey("user.id"), nullable=False)


class RoomAmenities(Base):
    id = Column(Integer, primary_key=True, index=True)

    room_id = Column(ForeignKey("room.id"))
    amenity_id = Column(ForeignKey("amenty.id"))


class Photo(Base):
    id = Column(Integer, primary_key=True, index=True)
    url = Column(Text)

    room_id = Column(ForeignKey("room.id"))
