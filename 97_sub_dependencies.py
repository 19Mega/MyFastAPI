
# Comprendiendo las subdependencias de operaciones de ruta
# video 124 del curso https://www.youtube.com/watch?v=zc5oBL8y8g0
# las cookies en swagger no se ven
# last_query string (cookie)

from fastapi import Cookie, Depends, FastAPI

app = FastAPI()


def query_extractor(q: str | None = None):
    return q


def query_or_cookie_extractor(
    q: str = Depends(query_extractor), last_query: str | None = Cookie(None)
):
    if not q:
        return last_query
    return q


@app.get("/items/")
async def read_items(query_or_default: str = Depends(query_or_cookie_extractor)):
    return {'q_or_cookie': query_or_default}