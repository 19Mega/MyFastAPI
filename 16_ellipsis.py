
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

# PROBAR DE OTRA MANERA NO ME ESTA FUNCIONANDO ANNOTATED PARA VER EL ...
# ... indica que el parametro de consulta q es requerido

@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)] = ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


