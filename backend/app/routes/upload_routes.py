from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil

from app.services.memory_service import save_memory
from vision.ocr import extract_text
from vision.object_detector import detect_objects

router = APIRouter()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@router.post("/upload/image")
async def upload_image(file: UploadFile = File(...)):

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ocr_text = extract_text(str(file_path))
    objects = detect_objects(str(file_path))

    memory = {
        "title": f"Image Memory - {file.filename}",
        "description": ocr_text,
        "objects": objects,
        "source": file.filename,
        "image": f"/uploads/{file.filename}"
    }

    save_memory(memory)

    return {
        "message": "Image uploaded and processed",
        "filename": file.filename,
        "ocr_text": ocr_text,
        "objects": objects
    }