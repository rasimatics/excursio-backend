from typing import List
from datetime import datetime

from app.core.service.base import BaseSqlAlchemyServiceWithLogging
from app.core.exceptions.service import ServiceException
from .security import check_password
from .repo import UserRepo
from .schema import UserCreate, UserUpdate, UserOut


class UserService(BaseSqlAlchemyServiceWithLogging[UserRepo]):
    async def create_user(self, db_session, user_in: UserCreate) -> UserOut:    
        # create user 
        db_obj = await self.repo.create(db_session, user_in.dict(exclude={"permissions"}))
        user = await self.get_user(db_session, id=db_obj.id)
        
        await db_session.commit()
        return UserOut(**user.__dict__)

    async def get_user(self, db_session, id) -> UserOut:
        user = await self.repo.get(db_session, id)
        return UserOut(**user.__dict__)

    async def get_all_users(self, db_session) -> List[UserOut]:
        users = await self.repo.get_all(db_session)
        return [UserOut(**user.__dict__) for user in users]
    
    async def update_user(self, db_session, user: UserOut, id, user_in: UserUpdate) -> UserOut:
        user_in = user_in.dict(exclude_unset=True)
        user = await self.repo.update(db_session, id, user_in)
        await db_session.commit()
        return UserOut(**user.__dict__)

    async def delete_user(self, db_session, id) -> None:
        await self.repo.delete(db_session, id=id)
        await db_session.commit()

    async def authenticate_user(self, db_session, email: str, password: str) -> UserOut:
        user = await self.repo.get_by_email(db_session, email=email)

        if not user:
            raise ServiceException("username or password is incorrect", status=400)

        if not check_password(password, user.password):
            raise ServiceException("username or password is incorrect", status=400)

        return UserOut(**user.__dict__)

        
