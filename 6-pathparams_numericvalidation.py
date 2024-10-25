from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get")],
#     q : Annotated[str|None, Query(alias="item-query")] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# alias ini artinya adalah nama lain jadi nanti ketika akses query parameter q, kita bisa menggunakan item-query
# ?item-query=ini adalah query parameter
# gt: greater than
# ge: greater than or equal
# lt: less than
# le: less than or equal
@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", gt=0, le=1000)],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results