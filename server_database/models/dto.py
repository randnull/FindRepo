from pydantic import BaseModel
from typing_extensions import Self, List
from models.orm import GlobalTable, LocalTable


class GlobalModel(BaseModel):
    hash: str
    links: List[str]

    @classmethod
    def from_orm(cls, obj: GlobalTable) -> Self:
        return GlobalModel(
            hash=obj.hash,
            links=obj.links
        )


class LocalModel(BaseModel):
    hashes: List[str]
    link: str

    @classmethod
    def from_orm(cls, obj: LocalTable) -> Self:
        return LocalModel(
            hashes=obj.hashes,
            link=obj.link
        )
