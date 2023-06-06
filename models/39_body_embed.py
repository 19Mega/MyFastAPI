from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# with out Body(embed=True)

#   {
#     "name": "string",
#     "description": "string",
#     "price": 0,
#       "tax": 0
#   }


# with Body(embed=True)
#   {
#     "item": {
#       "name": "string",
#       "description": "string",
#        "price": 0,
#       "tax": 0
#       }
#   }


@app.put('/items/{item_id}')
async def update_item(
    item_id: int,
    # item: Item = Body(embed=True) # mirar comentarios de arriba
    item: Item 
    
    
):
    results = {
        'item_id': item_id,
        'item': item
    }

    return results