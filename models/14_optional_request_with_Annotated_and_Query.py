from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

# NO ME FUNCIONO, o sea pongo valores mas alto que 2 y me acepta igual, lo mismo en el de abajo...


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=2)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results




@app.get("/itemsss/")
async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results