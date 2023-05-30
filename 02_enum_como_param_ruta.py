from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
from enum import Enum

class Item(str, Enum):
    item_1 = "Caja cuadrada"
    item_2 = "Caja rectangular"
    item_3 = "Caja plana"


app = FastAPI()


@app.get('/')
async def root():
    return {'Mensaje': 'Bienvenidos a Items'}


# USANDO ENUM PARA PARAMETROS NOS PERMITE TENER UNA LISTA DE PARAMETROS A ELEGIR
@app.get('/item/{item_box}')
async def get_item_name(item_box:Item):
    
    if item_box is Item.item_1:
        return{'Mensaje': f'El item escogido es: {Item.item_1.value}'}
    if item_box is Item.item_2:
        return{'Mensaje': f'El item escogido es: {Item.item_2.value}'}
    if item_box is Item.item_3:
        return{'Mensaje': f'El item escogido es: {Item.item_3.value}'}