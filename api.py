import shutil
from typing import List

from fastapi import APIRouter, File, Form, Request, UploadFile
from fastapi.responses import JSONResponse

from schemas import GetVideo, Message, UploadVideo, User

from models import Video

video_router = APIRouter()


@video_router.post('/')
async def create_video(title: str = Form(...),
                       description: str = Form(...),
                       file: UploadFile = File(...)):
    info = UploadVideo(title, description)
    with open(f'{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    user = await User.objects.first()

    return await Video.objects.create(file=file.filename, user=user, **info.dict)


@video_router.post('/img', status_code=201)
async def upload_image(file: List[UploadFile] = File(...)):
    for img in files:
        with open(f'{img.filename}', 'wb') as buffer:
            shutil.copy(img.file, buffer)

    return {'file_name': file.filename}


@video_router.post('/info')
async def info_set(info: UploadVideo):
    return info


@video_router.post('/video')
async def create_video(video: Video):
    await video.save()
    return video


@video_router.get('/video/{video_pk}',
                  response_model=Video,
                  responses={404: {
                      'model': Message
                  }})
async def get_video(video_pk: int):
    return await Video.objects.select_related('user').get(pk=video_pk)


@video_router.get('/test')
async def get_test(req: Request):
    print(req.user.dict())
    return {}