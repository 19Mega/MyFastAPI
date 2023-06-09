from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# El parámetro response_model_exclude_unset=True se utiliza para excluir 
# las propiedades del modelo Item que no se establecen en la respuesta. 
# Esto significa que si una propiedad no tiene un valor establecido en 
# la respuesta, se omitirá en la respuesta enviada al cliente. 
# Por ejemplo, si el objeto Item devuelto por read_item no tiene 
# una descripción establecida, la propiedad description se omitirá en la respuesta.

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []

# usamos esto como una base de datos
items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": None,
        "price": 50.2,
        "tax": 10.5,
        "tags": [],
    },
}

# devuelve un elemento de nuestra base de datos, le pasamos el nombre en el path >>> foo, bar, baz
@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]
