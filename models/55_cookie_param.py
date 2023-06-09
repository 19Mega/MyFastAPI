from fastapi import Cookie, FastAPI

app = FastAPI()

# solo se ve el valor asignado en el -H header, pero no lo retorna...

@app.get("/items/")
async def read_items(ads_id: str | None = Cookie(default=None)):
    return {"ads_id": ads_id}