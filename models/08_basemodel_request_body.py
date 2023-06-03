from fastapi import FastAPI
from pydantic import BaseModel

# Tener una clase con BaseModel permite y da una estructura para trabajar con el 
# objeto que recibimos e interactuamos en swagger (json)
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item