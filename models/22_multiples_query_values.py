from fastapi import FastAPI, Query

app = FastAPI()

# http://127.0.0.1:8000/items/?q=elemento%201&q=elemento%202&q=elemento%203&q=elemento%204&q=string
# %20 es un espacio en el query parameters
# sin espacios: http://127.0.0.1:8000/items/?q=elemento1&q=elemento2&q=elemento3&q=elemento4&q=elemento5


@app.get('/items/')
async def read_items(q: list[str] | None = Query(default=None)):
    query_items = {'q': q}

    return query_items