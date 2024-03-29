from fastapi import FastAPI, HTTPException, status

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}

#incluimos un encabezado personalizado en la respuesta (video 108 FastAPI - John Ortiz Ordoñez - youtube)

@app.get("/items-header/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": "Item not found", "item_id": item_id, 'code': status.HTTP_404_NOT_FOUND},
            headers={"X-Error": "There goes my error"},
        )
    
    return {"item": items[item_id]}