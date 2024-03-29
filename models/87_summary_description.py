
# Agregar un resumen y una descripción a una operación de ruta

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@app.post(
    "/items/",
    response_model=Item,
    tags=["items"],
    summary="Create an item and store it in the database",
    description="Create an item with all the information, name, description, price, tax and a set of unique tags",)
async def create_item(item: Item):
    return item