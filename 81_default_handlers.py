
# Sobrescritura de las excepciones de validación

from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

# con esto recibimos texto plano de respuesta (Nope, not going to do it), es como un override de la exception que levanta normalmente
# asi:
# {
#  "detail": "Nope, not going to do it."
# }
# Mas bien es con el primer exception, el 2do no se como funciona
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

# 2do
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope, not going to do it.")
    return {"item_id": item_id}