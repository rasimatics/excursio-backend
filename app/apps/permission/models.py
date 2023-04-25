from sqlalchemy import Column, Integer, String
from app.core.database.base import Base


class Permission(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=50), unique=True)

