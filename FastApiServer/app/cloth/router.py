##################
# fastapi/main.py
##################

import datetime
from fastapi import File, UploadFile, APIRouter
from typing import List
import os

from app.cloth.spec import Spec

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/now")
async def now():
    return {"now": datetime.datetime.now().strftime('%Y-%m-%d')}


@router.post("/files")
async def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}


@router.post("/files/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    UPLOAD_DIRECTORY = "./"
    for file in files:
        contents = await file.read()
        with open(os.path.join(UPLOAD_DIRECTORY, file.filename), "wb") as fp:
            fp.write(contents)
        print(file.filename)
    fname = [file.filename for file in files][0]
    return Spec.service(filename=fname)