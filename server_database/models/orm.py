from sqlalchemy import Column, String, Integer, ARRAY
from typing_extensions import Self
from repository.repository import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.dto import GlobalModel
    from models.dto import LocalModel


class GlobalTable(Base):
    __tablename__ = 'global-hash-table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hash = Column(String)
    links = Column(ARRAY(String))

    @classmethod
    def from_model(cls, obj: 'GlobalModel') -> Self:
        return GlobalTable(
            hash=obj.hash,
            links=obj.links
        )


class LocalTable(Base):
    __tablename__ = 'local-hash-table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hashes = Column(ARRAY(String))
    link = Column(String)

    @classmethod
    def from_model(cls, obj: 'LocalModel') -> Self:
        return LocalTable(
            hashes=obj.hashes,
            link=obj.link
        )
