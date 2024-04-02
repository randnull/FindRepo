from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from sqlalchemy import and_, cast, BOOLEAN
from sqlalchemy.ext.declarative import declarative_base
from typing import TypeVar, Generic, Type


Base = declarative_base()
T = TypeVar("T", bound=Base)


class AbstractRepository(Generic[T]):
    def __init__(self, session: AsyncSession, model_cls: Type[T]) -> None:
        self._session: AsyncSession = session
        self._table: T = model_cls

    async def get_all(self) -> Sequence[T]:
        result = await self._session.execute(select(self._table))
        return result.scalars().all()

    async def get_by_hash(self, hash: str) -> T | None:
        result = await self._session.execute(select(self._table).where(self._table.hash == hash))
        return result.scalars().one_or_none()

    async def get_by_id(self, id: int | UUID) -> T | None:
        result = await self._session.execute(select(self._table).where(self._table.id == id))
        return result.scalars().one_or_none()

    async def get_by_list(self, data: list) -> bool:
        z = zip(self._table.__table__.columns.keys()[1:], data)
        z = zip(self._table.__table__.columns.keys()[1:], data)
        result = await self._session.execute(
            select(self._table).where(and_(*[getattr(self._table, c) == d for c, d in z])))
        return result.scalars().one_or_none()

    async def add(self, table_cls: T) -> T | None:
        try:
            self._session.add(table_cls)
            await self._session.commit()
            await self._session.refresh(table_cls)
            return table_cls
        except:
            return None

    async def delete(self, table_cls: T) -> None:
        await self._session.delete(table_cls)
        await self._session.commit()

    async def delete_by_hash(self, hash: str) -> None:
        record = await self.get_by_hash(hash)
        if record is not None:
            await self._session.delete(record)
            await self._session.commit()

    async def delete_by_id(self, id: int) -> int:
        record = await self.get_by_id(id)
        if record is not None:
            await self._session.delete(record)
            await self._session.commit()
            return 1
        else:
            return 0

    async def get_by_field(self, field: str, value: int | str) -> Sequence[T]:
        result = await self._session.execute(
            select(self._table).where(cast(getattr(self._table, field) == value, BOOLEAN)))
        return result.scalars().all()

    async def update(self, table_cls: T, field: str, value: int | str) -> T:
        setattr(table_cls, field, value)
        await self._session.commit()
        await self._session.refresh(table_cls)
        return table_cls