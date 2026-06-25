from pathlib import Path

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".jpg",
    ".jpeg",
    ".png",
    ".webp"
}


def get_files(folder_path):

    files = []

    path = Path(folder_path)

    for file in path.rglob("*"):

        if (
            file.is_file()
            and file.suffix.lower()
            in ALLOWED_EXTENSIONS
        ):
            files.append(str(file))

    return files