from fastapi import FastAPI, Form

app = FastAPI()

# aca no podemos enviar parametros en json, tienen que ser en formato Form
# NO SE PUEDE USAR JSON PARA ENVIAR USERNAME/PASSWORDDDD

@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}