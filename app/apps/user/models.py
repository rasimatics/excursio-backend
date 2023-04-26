from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.core.database.base import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    bio = Column(Text)
    avatar = Column(String)
    is_active = Column(Boolean, server_default="true")
    role_id = Column(ForeignKey("role.id"), nullable=False)
    
    role = relationship("Role", backref="user")



