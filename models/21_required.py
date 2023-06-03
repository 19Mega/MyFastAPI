from fastapi import FastAPI, Query
from pydantic import Required

app = FastAPI()

# EN VEZ DE ... ELLIPSIS USAMOS REQUIRED, ES LO MISMO, SE USA LO QUE TE GUSTE MAS

@app.get('/items/')
async def read_items(q: str | None = Query(default=Required, min_length=3)):
    results = {
        'items': [
            {'item_id': 'ABC'},
            {'item_id': 'XYZ'}
        ]
    }

    if q:
        results.update({'q': q})
    
    return results