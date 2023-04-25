from fastapi.encoders import jsonable_encoder
from sqlalchemy import select, delete

class BaseRepo:
    pass


class BaseSqlalchemyRepo(BaseRepo):
    model = None

    async def create(self, session, obj_in):
        obj_in_dict = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_dict)
        session.add(db_obj)
        await session.flush()
        await session.refresh(db_obj)
        return db_obj

    async def get(self, session, id: int):
        stmt = select(self.model).where(self.model.id == id)
        result = await session.execute(stmt)
        return result.scalars().one_or_none()

    async def list(self, session):
        stmt = select(self.model)
        result = await session.execute(stmt)
        return result.scalars().all()

    async def update(self, session, db_obj: model, obj_in):
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        session.add(db_obj)
        await session.flush()
        await session.refresh(db_obj)
        return db_obj

    async def delete(self, session, id: int):
        stmt = delete(self.model).where(self.model.id == id)
        await session.execute(stmt)
        await session.flush()

