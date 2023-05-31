from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# http://127.0.0.1:8000/items/?skip=0&limit=10
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# Aqui nos va traer los 10 primeros elementos de fake_items_db, seria como una consulta (query)
# Pasamos los datos con el formato Key:Value que en el caso del path seria con Key=Value, cambia el : por =
# Arrancan con ? y lo separan un &
# todo el path es tipo str, pero al especificar los tipos en nuestra funcion, ya transformamos los valores al tipo que se indico

# EJEMPLO:
# https://www.amazon.com/s?k=ps5+controller&crid=3T6ZMHUZKU1QM&sprefix=%2Caps%2C185&ref=nb_sb_ss_recent_1_0_recent
# https://www.amazon.com/s?k=ps5+controller&rh=n%3A468642%2Cp_89%3APlayStation&dc&ds=v1%3AZ6goJQUA2a6so9beBX0RFhvMhbrjbcagV2G5R1hGVEQ&crid=3T6ZMHUZKU1QM&qid=1685475888&rnid=2528832011&sprefix=%2Caps%2C185&ref=sr_nr_p_89_1