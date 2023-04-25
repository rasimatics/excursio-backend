from typing import List
from datetime import datetime

from app.core.service.base import BaseSqlAlchemyServiceWithLogging
from app.core.exceptions.service import ServiceException
from .security import check_password
from .repo import UserRepo
from .schema import UserCreate, UserUpdate, UserOut


class UserService(BaseSqlAlchemyServiceWithLogging[UserRepo]):
    def __init__(self, repo, permission_service, logger):
        super().__init__(repo, logger)
        self.permission_service = permission_service

    async def create_user(self, db_session, user_in: UserCreate) -> UserOut:    
        # create user 
        db_obj = await self.repo.create(db_session, user_in.dict(exclude={"permissions"}))
        user = await self.get_user(db_session, id=db_obj.id)
        
        # set permissions
        permissions = await self.permission_service.get_permissions(db_session, ids=user_in.permissions)
        user.permissions = permissions
        
        await db_session.commit()
        return UserOut(**user.__dict__)

    async def get_user(self, db_session, id) -> UserOut:
        user = await self.repo.get(db_session, id)
        return UserOut(**user.__dict__)

    async def get_all_users(self, db_session) -> List[UserOut]:
        users = await self.repo.get_all(db_session)
        return [UserOut(**user.__dict__) for user in users]
    
    async def update_user(self, db_session, user: UserOut, id, user_in: UserUpdate) -> UserOut:
        if not user.get_role() == "is_admin" and user.id != id:
            raise ServiceException("Insufficent permissions", status=403)

        if user.get_role() == "is_admin":
            if user_in.permissions:
                user_in.permissions = await self.permission_service.get_permissions(db_session, ids=user_in.permissions)
            
            user_in = user_in.dict(exclude_unset=True)
        else:
            user_in = user_in.dict(
                exclude={"permissions", "user_id", "role_id", "email", "is_active", "company_code"}, exclude_unset=True
            )
        
        user = await self.repo.update(db_session, id, user_in)
        await db_session.commit()
        return UserOut(**user.__dict__)

    async def delete_user(self, db_session, id) -> None:
        await self.repo.delete(db_session, id=id)
        await db_session.commit()

    async def authenticate_user(self, db_session, username: str, password: str) -> UserOut:
        user = await self.repo.get_by_username(db_session, username=username)

        if not user:
            raise ServiceException("username or password is incorrect", status=400)

        if not check_password(password, user.password):
            raise ServiceException("username or password is incorrect", status=400)

        return UserOut(**user.__dict__)
    
    async def update_after_login(self, db_session, id: str, last_ip):
        last_ip = last_ip[0] if last_ip else None
        last_login = datetime.now()
        await self.repo.update_after_login(db_session, id, last_ip, last_login)
        await db_session.commit()


        
