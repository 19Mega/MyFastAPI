
# Dependencias sin usar caché

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
async def read_items(query_or_default: str = Depends(query_or_cookie_extractor, use_cache=False)):
    return {'q_or_cookie': query_or_default}