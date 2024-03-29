from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

# mix param: 
# path ( {items_id} )
# query(q) 
# body request (item: Item)

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put('/items/{item_id}')
async def update_item(*, 
                        item_id: int = Path(title='The ID of the item to get', ge=0, le=1000), 
                        q: str | None = None, 
                        item: Item | None = None
                        ):
    
    result = {'item_id': item_id}

    if q:
        result.update({'q': q})
    
    if item:
        result.update({'item': item})
    
    return result