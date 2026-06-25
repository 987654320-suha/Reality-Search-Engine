from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil

from document.pdf_reader import extract_pdf_text
from app.services.memory_service import save_memory

router = APIRouter()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/upload/pdf")
async def upload_pdf(
    file: UploadFile = File(...)
):

    file_path = (
        UPLOAD_DIR / file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    text = extract_pdf_text(
        str(file_path)
    )

    memory = {
        "title":
        f"PDF Memory - {file.filename}",

        "description": text,

        "source": file.filename,

        "file_type": "pdf"
    }

    save_memory(memory)

    return {
        "message":
        "PDF uploaded successfully",

        "filename":
        file.filename
    }