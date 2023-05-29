from pydantic import BaseModel
from typing import Union, Optional
from uuid import uuid4 as uuid

class Producto(BaseModel):
    id: Optional[str]
    nombre: str
    precio_compra: float
    precio_venta: float
    proveedor: str


#mochila = Producto(id=str(uuid()),nombre='pedro', precio_compra=100,precio_venta=120,proveedor='pedros proveedo sas')

#print(mochila)