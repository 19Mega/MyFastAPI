from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str = Field(example="Foo")
    description: str | None = Field(default=None, example="A very nice Item")
    price: float = Field(example=35.4)
    tax: float | None = Field(default=None, example=3.5)


@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results