from pydantic import BaseModel
from typing import Union


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None # uno de los datos va ser [bool o None], por defecto esta None

