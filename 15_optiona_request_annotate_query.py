from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

# NO FUNCIONA SI LE PASAS ALGO MENOR A length 3...

@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery"):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results