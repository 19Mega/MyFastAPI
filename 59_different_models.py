from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

# recibimos el UserIn y respondemos enviando el UserOut (sin la contraseña)
@app.post("/users/", response_model=UserOut)
async def create_user(user: UserIn):
    return user