from fastapi import APIRouter

from app.services.folder_indexer import get_files
from app.services.auto_importer import import_file

router = APIRouter()


@router.get("/index-folder")
def index_folder(path: str):

    files = get_files(path)

    imported = 0

    for file in files:

        if import_file(file):
            imported += 1

    return {
        "files_found": len(files),
        "imported": imported
    }