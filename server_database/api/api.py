from typing_extensions import Self, List
from fastapi import FastAPI, Response, Request, Depends
from pydantic import BaseModel
from repository.repository import AbstractRepository, get_repository
from models.dto import GlobalModel, LocalModel
from models.orm import GlobalTable, LocalTable


def get_local_rep():
    rep = get_repository(LocalTable)
    yield rep


def get_global_rep():
    rep = get_repository(GlobalTable)
    yield rep


def jaccard_set(list1, list2):
    """Define Jaccard Similarity function for two sets"""
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/global/add")
async def global_add(data: GlobalModel, repository: AbstractRepository = Depends(get_global_rep)):
    await repository.add(GlobalTable.from_model(data))
    return Response(status_code=200)


@app.get("/global/get/{hash}")
async def global_get(hash: str, repository: AbstractRepository = Depends(get_global_rep)):
    row = await repository.get_by_hash(hash)
    return GlobalModel.from_orm(row)


@app.post("/local/add")
async def local_add(data: LocalModel, repository: AbstractRepository = Depends(get_local_rep)):
    await repository.add(LocalTable.from_model(data))
    return Response(status_code=200)


@app.post("/local/get")
async def local_get(base_hashes: List[str], repository: AbstractRepository = Depends(get_local_rep)):
    rows = await repository.get_all()
    ans = []
    for r in rows:
        model_row = LocalModel.from_orm(r)
        if jaccard_set(base_hashes, model_row.hashes) >= 0.45:
            ans.append(model_row)
    return ans

