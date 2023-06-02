from fastapi import FastAPI, Query

app = FastAPI()

# ... indica que el parametro de consulta q es requerido
# ESTE FUNCIONA IMPECABLE, el de annoted no.

@app.get('/items')
async def read_items(q: str = Query(default=..., min_length=3)):
    results = {
        'items': [
            {'item_id': 'ABC'},
            {'item_id': 'XYZ'}
        ]
    }

    if q:
        results.update({'q': q})
    
    return results