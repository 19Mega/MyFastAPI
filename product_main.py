from fastapi import FastAPI
from models.product_model import Producto
from uuid import uuid4 as uuid


app = FastAPI()

productos = []

@app.get('/')
def root():
    return {'Mensaje':'Bienvenidos a productos'}

@app.get('/productos')
def get_productos():
    return productos

@app.get('/buscar/{product_id}')
def get_product_id(product_id:str):
    for producto in productos:
        if product_id == Producto.id:
            return producto
        else:
            return{'Mensaje':'No se ha encontrado ese producto'}


@app.post('/nuevoproducto')
def post_producto(nuevo_producto: Producto):
    nuevo_producto.id= str(uuid())
    productos.append(nuevo_producto)
    return{'Mensaje':'Un nuevo producto ha sido creado'}


