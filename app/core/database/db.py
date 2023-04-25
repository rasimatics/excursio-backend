from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Column, DateTime, func
from typing import Dict
from ..config.settings import app_settings


class_registry: Dict = {}

@as_declarative(class_registry=class_registry)
class Base:
    create_at = Column(DateTime(timezone=True), server_default=func.now())
    update_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()



DATABASE_URL = app_settings.DB_URI
_engine = create_async_engine(DATABASE_URL)
SessionLocal = async_sessionmaker(bind=_engine, expire_on_commit=False)

