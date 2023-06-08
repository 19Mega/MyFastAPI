from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] | None = []

# esto retorna un objeto item, si le ponemos return {"otra":"cosa"} da error
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item
