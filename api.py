import shutil
from typing import List

from fastapi import APIRouter, File, Form, Request, UploadFile
from fastapi.responses import JSONResponse

from schemas import GetVideo, Message, UploadVideo, User

video_router = APIRouter()


@video_router.post('/')
async def root(title: str = Form(...),
               description: str = Form(...),
               file: UploadFile = File(...)):
    info = UploadVideo(title, description)
    with open(f'{file.filename}', 'wb') as buffer:
        shutil.copy(file.file, buffer)

    return {'file_name': file.filename, 'info': info}


@video_router.post('/img', status_code=201)
async def upload_image(file: List[UploadFile] = File(...)):
    for img in files:
        with open(f'{img.filename}', 'wb') as buffer:
            shutil.copy(img.file, buffer)

    return {'file_name': file.filename}


@video_router.post('/info')
async def info_set(info: UploadVideo):
    return info


@video_router.get('/video',
                  response_model=GetVideo,
                  responses={404: {
                      'model': Message
                  }})
async def get_video():
    user = {'id': 10, 'name': 'Taras'}
    video = {'title': 'Test', 'description': 'Description'}
    info = GetVideo(user=user, video=video)
    return JSONResponse(status_code=200, content=info.dict())



@video_router.get('/test')
async def get_test(req: Request):
    print(req.user.dict())
    return {}