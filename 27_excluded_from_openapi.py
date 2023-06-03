from fastapi import FastAPI, Query

app = FastAPI()

# SI LE PASAMOS ESTO LO RECIBE BIEN http://127.0.0.1:8000/items/?hidden_query=monitor
# ES UNA QUERY ESCONDIDA

@app.get('/items/')
async def read_items(hidden_query: str | None = Query(default=None, include_in_schema=False)):
    
    if hidden_query:
        return {'hidden_query': hidden_query}
    else:
        return {'hidden_query': 'Not found'}