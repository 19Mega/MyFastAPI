from fastapi import FastAPI, Path

app = FastAPI()

# aca en python el * no significa nada, pero fastapi va saber que todos los 
# prodimos elementos que se agreguen van a ser kwargs, o sea todos con key-value clave-valor

@app.get('/items/{item_id}')
async def read_items(*, item_id: int = Path(title='The ID of the item to get'), q: str):
    results = {'item_id': item_id}

    if q:
        results.update({'q': q})
    
    return results