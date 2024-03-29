# tags (etiquetas de titulo) para swagger, para que quede bonito y organizado

# Uso de la configuración de etiquetas para operaciones de ruta

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@app.post("/items/", response_model=Item, tags=["items"])
async def create_item(item: Item):
    return item


@app.get("/items/", tags=["items"])
async def read_items():
    return [{'name': 'foo', 'price': 42}]


@app.get("/users/", tags=["users"])
async def read_users():
    return [{'username': 'johno'}]

