from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.core.database.base import Base


class UserPermission(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    perm_id = Column(Integer, ForeignKey("permission.id"))



class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    company_code = Column(Integer, nullable=False)
    user_id = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    dep_name = Column(String)
    position = Column(String)
    last_ip = Column(String)
    roc_limit = Column(Integer)
    last_login = Column(DateTime)
    contract_date = Column(Date)
    is_active = Column(Boolean, server_default="true")
    role_id = Column(ForeignKey("role.id"), nullable=False)
    
    role = relationship("Role", backref="user")
    permissions = relationship("Permission", secondary="userpermission")




