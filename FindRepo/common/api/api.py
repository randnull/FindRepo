from typing_extensions import Self, List
from fastapi import FastAPI, Response, Request, Depends
from pydantic import BaseModel
from repository.repository import get_local_rep, get_global_rep, AbstractRepository, GlobalTable, LocalTable


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
    hash: str
    links: List[str]

    @classmethod
    def from_orm(cls, obj: LocalTable) -> Self:
        return GlobalModel(
            hashes=obj.hashes,
            links=obj.links
        )


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/global/add")
async def local_add(hash: str, repository: AbstractRepository = Depends(get_global_rep)):
    await repository.add(GlobalTable(hash=hash, links=[]))
    return Response(200)


@app.post("/global/update/{hash}")
async def local_update(hash: str, link: str, repository: AbstractRepository = Depends(get_global_rep)):
    row = await repository.get_by_hash(hash)
    await repository.update_links(row, link)
    return Response(200)


@app.get("/global/get")
async def global_get(repository: AbstractRepository = Depends(get_global_rep)):
    rows = await repository.get_all()
    return [GlobalModel.from_orm(x) for x in rows]


@app.post("/local/add")
async def local_add(hashes: List[str], repository: AbstractRepository = Depends(get_local_rep)):
    await repository.add(LocalTable(hashes))


@app.get("/local/get")
async def local_get(repository: AbstractRepository = Depends(get_local_rep)):
    rows = await repository.get_all()
    return [LocalModel.from_orm(x) for x in rows]
