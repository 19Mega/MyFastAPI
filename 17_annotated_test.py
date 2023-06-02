from typing import Annotated

from fastapi import FastAPI, Query, HTTPException

app = FastAPI()

# FUNCIONA ANNOTATED, pero esta medio forzado.. no se

@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3, max_length=50)]):
    if len(q) < 3:
        raise HTTPException(status_code=400, detail="El parámetro 'q' debe tener una longitud mínima de 3 caracteres.")
    
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
