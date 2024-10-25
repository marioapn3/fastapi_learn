from fastapi import FastAPI, status

app = FastAPI()


# response status code 200
@app.get("/")
async def read_root():
    return {"message": "Hello World"}

# response status code 200
@app.get("/items/{item_id}", status_code=status.HTTP_200_OK)
async def read_item(item_id: int):
    return {"item_id": item_id}

# response status code 201
@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}