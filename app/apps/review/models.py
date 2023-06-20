from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.database.base import Base


class Review(Base):
    id = Column(Integer, primary_key=True, index=True)
    comment = Column(Text)
    stars = Column(Integer, nullable=False)

    user_id = Column(ForeignKey("user.id"), nullable=False)
    room_id = Column(ForeignKey("room.id"), nullable=False)

    user = relationship("User", backref="reviews")


