# creacion de una aplicacion FastAPI
from typing import Union
from fastapi import FastAPI
from models.item_model import Item
from uuid import uuid4 as uuid


app = FastAPI()


# GET
@app.get('/')
def read_root():
    return {"Hello" : "World"}

# le pasamos el {item_id} por path y lo recibimos en la funcion
@app.get("/items/{item_id}") 
async def read_item(item_id: int):
    return {"item_id": item_id}

# asi le pasamos los parametros: http://127.0.0.1:8000/calculadora?param_1=5&param_2=10
@app.get("/calculadora")
async def calcular(param_1: float, param_2: float):
    return {'La suma es igual a ': param_1 + param_2}


# PUT - UPDATE
@app.put('/items/{item_id}') # en item_id va a quien queremos updatear
def update_item(item_id: int, item: Item): # por path [item_id] + [item] que son los datos que queremos updatear
    return {'item_name': item.name, 'item_id': item_id, 'item_price': item.price}