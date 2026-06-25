from pathlib import Path
import shutil

from vision.ocr import extract_text
from vision.object_detector import detect_objects
from document.pdf_reader import extract_pdf_text
from document.docx_reader import extract_docx_text

from app.services.memory_service import (
    save_memory,
    load_memories
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


def import_file(file_path):

    path = Path(file_path)

    suffix = path.suffix.lower()

    allowed_extensions = [
        ".jpg",
        ".jpeg",
        ".png",
        ".webp",
        ".pdf",
        ".docx"
    ]

    if suffix not in allowed_extensions:
        return False

    memories = load_memories()

    # Skip duplicates
    for memory in memories:

        if memory.get("source") == str(path):
            return False

    try:

        # IMAGE FILES
        if suffix in [
            ".jpg",
            ".jpeg",
            ".png",
            ".webp"
        ]:

            destination = (
                UPLOAD_DIR / path.name
            )

            if not destination.exists():

                shutil.copy2(
                    path,
                    destination
                )

            text = extract_text(
                str(path)
            )

            objects = detect_objects(
                str(path)
            )

            memory = {
                "title":
                f"Image Memory - {path.name}",

                "description":
                text,

                "objects":
                objects,

                "source":
                str(path),

                "image":
                f"/uploads/{path.name}"
            }

            save_memory(memory)

            return True

        # PDF FILES
        elif suffix == ".pdf":

            text = extract_pdf_text(
                str(path)
            )

            memory = {
                "title":
                f"PDF Memory - {path.name}",

                "description":
                text,

                "source":
                str(path),

                "file_type":
                "pdf"
            }

            save_memory(memory)

            return True

        # DOCX FILES
        elif suffix == ".docx":

            text = extract_docx_text(
                str(path)
            )

            memory = {
                "title":
                f"DOCX Memory - {path.name}",

                "description":
                text,

                "source":
                str(path),

                "file_type":
                "docx"
            }

            save_memory(memory)

            return True

    except Exception as e:

        print(
            "IMPORT ERROR:",
            file_path,
            e
        )

    return False