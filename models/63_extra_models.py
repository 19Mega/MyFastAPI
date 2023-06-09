from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

# Aca tenemos un ejemplo de ingreso de usuario, como mostrarlo, y como guardarlo. 
# notese que el hashed es a modo de ejemplo, pero es lo que se usa, en la bd va la pass hasheada

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: str | None = None


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in_db: UserIn):
    hashed_password = fake_password_hasher(user_in_db.password)
    # El **user_in_db.dict() se usa para expandirlo y ensamblarlo en la clase UserInDB. 
    # Es como empaquetar todos los atributos y le agregamos el hashed_password.
    # user_dict = user_in.dict()
    # UserInDB = (**user_dict)
    user_in_db = UserInDB(**user_in_db.dict(), hashed_password=hashed_password) # se lo expande con ** para ponerlo en la clase 
    print('User saved! ..not really')
    print('hashed password: ', hashed_password)
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved