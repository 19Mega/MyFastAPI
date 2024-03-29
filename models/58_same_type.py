from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

# retornar el mismo dato de entrada

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


@app.post("/users/", response_model=UserIn)
async def create_user(user: UserIn):
    return user