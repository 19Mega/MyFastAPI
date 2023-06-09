from fastapi import FastAPI

app = FastAPI()

# si bien en el body request tenemos que pasar los int con "1": 2.5, 
# fastapi nos hace la conversion a int, asi que no preocupar
'''
Response body:
{
  "1": 1.6,
  "2": 2.8,
  "3": -1.5
}
'''

@app.post('/index-weights/')
async def create_index_weights(weights: dict[int, float]):
    return weights