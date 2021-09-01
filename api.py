import shutil
from uuid import uuid4
from http.client import HTTPException
from typing import List
from starlette.templating import JinjaTemplates

from fastapi import (APIRouter, File, Form, Request, UploadFile, HTTPException,
                     BackgroundTasks)
from fastapi.responses import JSONResponse
from starlette.responses import HTMLResponse, StreamingResponse

from models import Video, User
from schemas import GetListVideo, GetVideo, Message, UploadVideo

from services import save_video

video_router = APIRouter()


templates = JinjaTemplates(directory="templates")


@video_router.post('/')
async def create_video(background_tasks: BackgroundTasks,
                       title: str = Form(...),
                       description: str = Form(...),
                       file: UploadFile = File(...)):
    user = await User.objects.first()

    return await save_video(user.dict().get("id"), file, title, description,
                            background_tasks)


@video_router.get('/video/{video_pk}')
async def get_video(video_pk: int):
    file = await Video.objects.select_related('user').get(pk=video_pk)
    file_like = open(file.file, mode='rb')
    return StreamingResponse(file_like, media_type='video/mp4')


@video_router.get('/user/{user_pk}', response_model=List[GetListVideo])
async def get_list_video(user_pk: int):
    video_list = await Video.objects.filter(user=user_pk).all()
    return video_list


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


# @video_router.get('/video/{video_pk}',
#                   response_model=Video,
#                   responses={404: {
#                       'model': Message
#                   }})
# async def get_video(video_pk: int):
#     file = await Video.objects.select_related('user').get(pk=video_pk)
#     file_like = open(file.dict().get('file'), mode='rb')
#     return StreamingResponse(file_like, media_type='video/mp4')


# @video_router.get("/index/{video_pk}", response_class=HTMLResponse)
# async def get_video(request: Request, video_pk: int):
#     return templates.TemplateResponse("index.html", {"request": request, "path": video_pk})