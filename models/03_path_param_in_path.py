# PATH PARAM CONTAINING PATH

from fastapi import FastAPI

app = FastAPI()


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# You could need the parameter to contain /home/johndoe/myfile.txt, with a leading slash (/).
# In that case, the URL would be: /files//home/johndoe/myfile.txt, with a double slash (//) between files and home.


@app.get("/files2/{file_path:path}")
async def read_file(file_path: str):
    try:
        with open(file_path, "r") as file:
            content = file.read()
        return {"file_content": content}
    except FileNotFoundError:
        return {"error": "El archivo no existe"}
    
# Cuando un cliente realiza una solicitud GET a la ruta /files/abc/def/test.txt, 
# FastAPI capturará el valor "abc/def/test.txt" y lo asignará a la variable file_path. 
# Ahora puedes utilizar este valor en tu lógica para, por ejemplo, abrir y leer el 
# archivo correspondiente a esa ruta.