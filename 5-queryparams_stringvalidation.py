from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

# Not required query parameter dengan validasi string
@app.get("/not-required/")
async def read_items(
    q : Annotated[
        str | None,
        Query(
            min_length=3,
            max_length=50,
        ) 
    ]  = None
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# default value query parameter dengan validasi string
@app.get("/default-value/")
async def read_items(
        q : Annotated[
        str, 
        Query(
            min_length=3,
            max_length=50,
        )
    ] = "default"
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# required query parameter dengan validasi string
@app.get('/required/')
async def read_items(
    q : Annotated[
        str | int,
        Query(
            min_length=3,
            max_length=50,
        )
    ]
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# query dengan validasi list    
@app.get('/list')
async def read_items(
    q : Annotated[
        list[str] | None,
        Query()
    ] = None 
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

    # menyembunyikan paramter query dari dokumentasi
@app.get('/hidden/')
async def read_items(
    q : Annotated[
        str | None,
        Query(
            min_length=3,
            max_length=50,
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            deprecated=True
        )
    ] = None
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
