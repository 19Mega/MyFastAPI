from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

# basicamente una lista de imagenes, con sus respectivos enlaces.


class Image(BaseModel):
    url: HttpUrl
    name: str


@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
    return images