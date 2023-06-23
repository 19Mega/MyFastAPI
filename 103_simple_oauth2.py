
# Documentación extra para las funciones de autenticación

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel


# Datos de prueba para simular una base de datos:
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

app = FastAPI()



def fake_hash_password(password: str):
    """
    Simula una función de hash de contraseña.
    """
    return "fakehashed" + password


ouath2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str

def get_user(db, username: str):
    """
    Simula una función que obtiene un usuario de una base de datos.
    """
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
    

def fake_decode_token(token):
    """
    Simula una función que decodifica un token JWT.
    """
    user = get_user(fake_users_db, token)
    return user


async def get_current_user(token: str = Depends(ouath2_scheme)):
    """
    Simula una función que obtiene un usuario actual a partir de un token.    
    """
    user = fake_decode_token(token)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    """
    Simula una función que obtiene un usuario actual activo a partir de un token.
    """
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    
    return current_user


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user