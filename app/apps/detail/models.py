from sqlalchemy import Column, Integer, String, Text
from app.core.database.base import Base


class RoomDetail(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=50), unique=True)
    icon = Column(String(length=50))
    description = Column(Text)


