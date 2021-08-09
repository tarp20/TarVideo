import shutil
# import aiofiles

from fastapi import UploadFile



def write_video(file_name: str, file: UploadFile):

    # async with aiofiles.open(file_name, 'wb') as buffer:  async version
    #     data = await file.read()
    #     await buffer.write(data)


    with open(file_name, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)