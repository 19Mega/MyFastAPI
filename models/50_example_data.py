from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# CLASE CON CLASE DENTRO
# ES COMO PARA PRESENTAR UN EJEMPLO DE ESA CLASE
# CLASE ANIDADA
# NOS SIRVE PARA PRESENTAR EJEMPLO EN NUESTRA DOCUMENTACION

# En el 50 ponemos los ejemplos como clase
# En el 51 ponemos como metada (con el atributo example="algo")
# En el 52 lo ponemos en la funcion despues de nuestro decorador

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }


@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results