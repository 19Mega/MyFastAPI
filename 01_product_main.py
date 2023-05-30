from fastapi import FastAPI
# from models.product_model import Producto



from pydantic import BaseModel
from typing import Union, Optional
from uuid import uuid4 as uuid

class Producto(BaseModel):
    id: Optional[str]
    nombre: str
    precio_compra: float
    precio_venta: float
    proveedor: str




app = FastAPI()

productos = []

@app.get('/')
def root():
    return {'Mensaje':'Bienvenidos a productos.'}

# BUSCA TODOS LOS PRODUCTOS
@app.get('/productos')
def get_productos():
    return productos

# BUSCAR PRODUCTO
@app.get('/buscar/{product_id}')
def get_product_id(product_id:str):
    for p in productos:
        if p.id == product_id:
            return p
    
    return{'Mensaje':'No se ha encontrado ese producto.'}

# CREAR PRODUCTO
@app.post('/nuevoproducto')
def post_producto(nuevo_producto: Producto):
    nuevo_producto.id= str(uuid())
    productos.append(nuevo_producto)
    return{'Mensaje':'Un nuevo producto ha sido creado.'}

# ELIMINAR PRODUCTO
@app.delete('/eliminar/{producto_id}')
def eliminar_producto_por_id(product_id:str):
    for p in productos:
        if p.id == product_id:
            productos.remove(p)
            return{'Mensaje':f'Producto {p} eliminado correctamente.'}
        
    return{'Mensaje':f'Producto {p} no encontrado.'}

# ACTUALIZAR PRODUCTO
@app.put('/modificar/{product_id}')
def actualizar_producto_con_id(product_id:str, producto:Producto):
    for p in productos:
        if p.id == product_id:
            p.nombre = producto.nombre
            p.precio_compra = producto.precio_compra
            p.precio_venta = producto.precio_venta
            p.proveedor = producto.proveedor
            return {'Mensaje':f'Producto con ID:{product_id} fue actualizado correctamente.'}
    
    return {'Mensaje':f'Producto {product_id} no se encontro en la base de datos.'}