from typing import Sequence
from sqlalchemy import select, Column, String, Integer, ARRAY
from uuid import UUID
from sqlalchemy import and_, cast, BOOLEAN, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import TypeVar, Generic, Type

Base = declarative_base()
T = TypeVar("T", bound=Base)

engine = create_engine('postgresql://admin:admin@localhost:5432/hash_data', echo=True)
Session = sessionmaker(engine, expire_on_commit=False)


class Table(Base):
    __tablename__ = 'hash-table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hash = Column(String)
    links = Column(ARRAY(String))


class AbstractRepository(Generic[T]):
    def __init__(self, model_cls: Type[T]) -> None:
        self._session = Session()
        self._table: T = model_cls

    def get_all(self) -> Sequence[T]:
        result = self._session.execute(select(self._table))
        return result.scalars().all()

    def get_by_hash(self, hash: str) -> T | None:
        result = self._session.execute(select(self._table).where(self._table.hash == hash))
        return result.scalars().one_or_none()

    def get_by_id(self, id: int | UUID) -> T | None:
        result = self._session.execute(select(self._table).where(self._table.id == id))
        return result.scalars().one_or_none()

    def get_by_list(self, data: list) -> bool:
        z = zip(self._table.__table__.columns.keys()[1:], data)
        result = self._session.execute(
            select(self._table).where(and_(*[getattr(self._table, c) == d for c, d in z])))
        return result.scalars().one_or_none()

    def add(self, table_cls: T) -> T | None:
        try:
            self._session.add(table_cls)
            self._session.commit()
            self._session.refresh(table_cls)
            return table_cls
        except:
            return None

    def delete(self, table_cls: T) -> None:
        self._session.delete(table_cls)
        self._session.commit()

    def delete_by_hash(self, hash: str) -> None:
        record = self.get_by_hash(hash)
        if record is not None:
            self._session.delete(record)
            self._session.commit()

    def delete_by_id(self, id: int) -> int:
        record = self.get_by_id(id)
        if record is not None:
            self._session.delete(record)
            self._session.commit()
            return 1
        else:
            return 0

    def get_by_field(self, field: str, value: int | str) -> Sequence[T]:
        result = self._session.execute(
            select(self._table).where(cast(getattr(self._table, field) == value, BOOLEAN)))
        return result.scalars().all()

    def update(self, table_cls: T, field: str, value: int | str) -> T:
        setattr(table_cls, field, value)
        self._session.commit()
        self._session.refresh(table_cls)
        return table_cls
