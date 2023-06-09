from fastapi import FastAPI, Form

app = FastAPI()

# aca no podemos enviar parametros en json, tienen que ser en formato Form
# NO SE PUEDE USAR JSON PARA ENVIAR USERNAME/PASSWORDDDD
# EL FORM SE USA CON EL PROTOCOLO HTTP, o sea para los datos que vienen desde un formulario, ej: login, crear usuario, etc

@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}