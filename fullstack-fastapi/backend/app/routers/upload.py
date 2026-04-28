from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import os

router = APIRouter()

UPLOAD_DIR = "uploads"

@router.post("/")
def upload_file(file: UploadFile = File(...)):
    path = os.path.join(UPLOAD_DIR, file.filename)
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}

@router.get("/{filename}")
def download_file(filename: str):
    path = os.path.join(UPLOAD_DIR, filename)
    return FileResponse(path)