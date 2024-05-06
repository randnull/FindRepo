from typing import Sequence
from sqlalchemy import select, Column, String, Integer, ARRAY
from uuid import UUID
from sqlalchemy import and_, cast, BOOLEAN, create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import TypeVar, Generic, Type

Base = declarative_base()
T = TypeVar("T", bound=Base)

engine = create_async_engine('postgresql+asyncpg://admin:admin@localhost:5432/hash_data', echo=True)
Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class GlobalTable(Base):
    __tablename__ = 'hash-table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hash = Column(String)
    links = Column(ARRAY(String))


class LocalTable(Base):
    __tablename__ = 'hash-table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hashes = Column(ARRAY(String))
    links = Column(ARRAY(String))


class AbstractRepository(Generic[T]):
    def __init__(self, model_cls: Type[T]) -> None:
        self._session = Session
        self._table: T = model_cls

    async def get_all(self) -> Sequence[T]:
        async with self._session() as session:
            result = session.execute(select(self._table))
            return result.scalars().all()

    def get_by_hash(self, hash: str) -> T | None:
        async with self._session() as session:
            result = session.execute(select(self._table).where(self._table.hash == hash))
            return result.scalars().one_or_none()

    def get_by_id(self, id: int | UUID) -> T | None:
        async with self._session() as session:
            result = session.execute(select(self._table).where(self._table.id == id))
            return result.scalars().one_or_none()

    def get_by_list(self, data: list) -> bool:
        async with self._session() as session:
            z = zip(self._table.__table__.columns.keys()[1:], data)
            result = session.execute(
                select(self._table).where(and_(*[getattr(self._table, c) == d for c, d in z])))
            return result.scalars().one_or_none()

    def add(self, table_cls: T) -> T | None:
        async with self._session() as session:
            try:
                session.add(table_cls)
                session.commit()
                session.refresh(table_cls)
                return table_cls
            except:
                return None

    def delete(self, table_cls: T) -> None:
        async with self._session() as session:
            session.delete(table_cls)
            session.commit()

    def delete_by_hash(self, hash: str) -> None:
        async with self._session() as session:
            record = self.get_by_hash(hash)
            if record is not None:
                session.delete(record)
                session.commit()

    def delete_by_id(self, id: int) -> int:
        async with self._session() as session:
            record = self.get_by_id(id)
            if record is not None:
                session.delete(record)
                session.commit()
                return 1
            else:
                return 0

    def get_by_field(self, field: str, value: int | str) -> Sequence[T]:
        async with self._session() as session:
            result = session.execute(
                select(self._table).where(cast(getattr(self._table, field) == value, BOOLEAN)))
            return result.scalars().all()

    def update(self, table_cls: T, field: str, value: int | str) -> T:
        async with self._session() as session:
            setattr(table_cls, field, value)
            session.commit()
            session.refresh(table_cls)
            return table_cls

    def update_links(self, table_cls: T, value: str) -> T:
        async with self._session() as session:
            table_cls.links.append(value)
            session.commit()
            session.refresh(table_cls)
            return table_cls


async def get_repository(table: Type[T]):
    return AbstractRepository(table)


async def get_local_rep():
    yield get_repository(LocalTable)


async def get_global_rep():
    yield get_repository(GlobalTable)
