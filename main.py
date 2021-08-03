import shutil
from typing import List
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post('/')
async def upload(file: UploadFile = File(...)):
    with open(f'{file.filename}', 'wb') as buffer:
        shutil.copy(file.file, buffer)

    return {'file_name': file.filename}


 
@app.post('/img')
async def upload_image(file: List[UploadFile] = File(...)):
    for img in files:
        with open(f'{img.filename}', 'wb') as buffer:
            shutil.copy(img.file, buffer)

    return {'file_name': file.filename}
