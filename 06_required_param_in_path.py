from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item


# http://127.0.0.1:8000/items/foo-item >>> ERROR
# http://127.0.0.1:8000/items/foo-item?needy=sooooneedy >>> BIEN