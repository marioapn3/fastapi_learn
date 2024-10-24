from fastapi import FastAPI
from enum import Enum

app = FastAPI()

# query parameter
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.get("/data/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# required query parameter
# needy ini adalah required query parameter karena tidak memiliki nilai default
# @app.get("/required/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     item = {"item_id": item_id, "needy": needy}
#     return item




@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

# case diatas terdapat 3 query parameter, yaitu item_id, needy, skip, dan limit
# item_id dan needy adalah required query parameter
# skip dan limit adalah optional query parameter
# skip memiliki nilai default 0
# limit tidak memiliki nilai default, sehingga di beri tanda | None
# jika limit tidak diisi, maka limit akan bernilai None