from typing_extensions import Sequence, Self
from sqlalchemy import select, Column, String, Integer, ARRAY
from uuid import UUID
from sqlalchemy import and_, cast, BOOLEAN
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from typing import TypeVar, Generic, Type

Base = declarative_base()
T = TypeVar("T", bound=Base)

engine = create_async_engine('postgresql+asyncpg://admin:admin@postgresql:5432/hash_data', echo=True)
Session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class AbstractRepository(Generic[T]):
    def __init__(self, model_cls: Type[T]) -> None:
        self._session = Session
        self._table: T = model_cls

    async def get_all(self) -> Sequence[T]:
        async with self._session() as session:
            result = await session.execute(select(self._table))
            return result.scalars().all()

    async def get_by_hash(self, hash: str) -> T | None:
        async with self._session() as session:
            result = await session.execute(select(self._table).where(self._table.hash == hash))
            return result.scalars().one_or_none()

    async def get_by_id(self, id: int | UUID) -> T | None:
        async with self._session() as session:
            result = await session.execute(select(self._table).where(self._table.id == id))
            return result.scalars().one_or_none()

    async def get_by_list(self, data: list) -> bool:
        async with self._session() as session:
            z = zip(self._table.__table__.columns.keys()[1:], data)
            result = await session.execute(
                select(self._table).where(and_(*[getattr(self._table, c) == d for c, d in z])))
            return result.scalars().one_or_none()

    async def add(self, table_cls: T) -> T | None:
        async with self._session() as session:
            session.add(table_cls)
            await session.commit()
            await session.refresh(table_cls)
            return table_cls

    async def delete(self, table_cls: T) -> None:
        async with self._session() as session:
            await session.delete(table_cls)
            await session.commit()

    async def delete_by_hash(self, hash: str) -> None:
        async with self._session() as session:
            record = await self.get_by_hash(hash)
            if record is not None:
                await session.delete(record)
                await session.commit()

    async def delete_by_id(self, id: int) -> int:
        async with self._session() as session:
            record = await self.get_by_id(id)
            if record is not None:
                await session.delete(record)
                await session.commit()
                return 1
            else:
                return 0

    async def get_by_field(self, field: str, value: int | str) -> Sequence[T]:
        async with self._session() as session:
            result = await session.execute(
                select(self._table).where(cast(getattr(self._table, field) == value, BOOLEAN)))
            return result.scalars().all()

    async def update(self, table_cls: T, field: str, value: int | str) -> T:
        async with self._session() as session:
            setattr(table_cls, field, value)
            await session.commit()
            await session.refresh(table_cls)
            return table_cls

    async def update_links(self, table_cls: T, value: str) -> T:
        async with self._session() as session:
            table_cls.links.append(value)
            await session.commit()
            await session.refresh(table_cls)
            return table_cls


def get_repository(table: Type[T]):
    return AbstractRepository(table)
