from sqlalchemy import Column, Integer, Float, ForeignKey, Date
from sqlalchemy.orm import relationship

from app.core.database.base import Base


class Reservation(Base):
    id = Column(Integer, primary_key=True, index=True)
    check_in = Column(Date)
    check_out = Column(Date)
    price = Column(Float)
    
    user_id = Column(ForeignKey("user.id"), nullable=False)
    room_id = Column(ForeignKey("room.id"), nullable=False)

    room = relationship("Room", backref="reservations")

