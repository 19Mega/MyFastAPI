from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: int | None = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

# In this case, there are 3 query parameters:

# needy, a required str.
# skip, an int with a default value of 0.
# limit, an optional int.
# Tip: You could also use Enums the same way as with Path Parameters.