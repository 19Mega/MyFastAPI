from fastapi import FastAPI, Path

app = FastAPI()

# el ge = 1 es: es una abreviatura de "greater than or equal" 

# lt (less than): verifica que el valor sea menor que el valor especificado.
# le (less than or equal): verifica que el valor sea menor o igual que el valor especificado.
# gt (greater than): verifica que el valor sea mayor que el valor especificado.
# ne (not equal): verifica que el valor no sea igual al valor especificado.
# ge (greater than or equal): verifica que el valor sea mayor o igual que el valor especificado.

@app.get('/items/{item_id}')
async def read_items(*, item_id: int = Path(title='The ID of the item to get', lt=1), q: str):
    results = {'item_id': item_id}

    if q:
        results.update({'q': q})
    
    return results