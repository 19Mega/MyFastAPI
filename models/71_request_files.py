from fastapi import FastAPI, File, UploadFile

app = FastAPI()

# el objeto File() se guarda en memoria como un array de bytes, tambien podemos
# acceder a los metadatos de este archivo mediante File(), por ejemplo len(file)
# return {"filename": file.filename, "filesize": file.size, "file headers": file.headers}

@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}
    