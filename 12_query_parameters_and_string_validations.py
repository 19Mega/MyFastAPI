from fastapi import FastAPI

app = FastAPI()

# Esto usa UNION (cuando vemos el | pipe, es UNION para valores opcionales) 
# aunque no este implicito y no se importe (ya viene con python), nos ayuda en la validacion de los tipos
@app.get("/items/")
async def read_items(q: str | None = None): 
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results