from fastapi import FastAPI

app = FastAPI()

# A TENER EN CUENTA:
# EQUIVALENCIA SEMANTICA >>>   0 = False = None   ó  1 = True = not False = "something"

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q}) # con item.update actualizamos el diccionario, agrega el item "q":q
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
        
    return item