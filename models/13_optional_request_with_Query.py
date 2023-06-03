from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")                 # Query(El por defecto es None y si viene un str que sea de maximo 10 de largo)
async def read_items(q:str | None = Query(default = None, max_length=10 )):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results