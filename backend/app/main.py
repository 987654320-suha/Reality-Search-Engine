from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.routes.memory_routes import router as memory_router
from app.routes.upload_routes import router as upload_router
from app.routes.search_routes import router as search_router
from app.routes.timeline_routes import router as timeline_router

from app.routes.chat_routes import router as chat_router
from app.routes.pdf_routes import (
    router as pdf_router
)
from app.routes.index_routes import (
    router as index_router
)
from app.services.folder_watcher import start_watcher

from app.routes.stats_routes import (
    router as stats_router
)
from app.routes.memory_details_routes import (
    router as memory_details_router
)

app = FastAPI(
    title="Reality Search Engine",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(memory_router)
app.include_router(upload_router)
app.include_router(search_router)
app.include_router(timeline_router)
app.include_router(chat_router)
app.include_router(pdf_router)
app.include_router(index_router)
app.include_router(stats_router)
app.include_router(
    memory_details_router
)

app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads"
)
@app.on_event("startup")
def startup_event():

    folders = [

        r"C:\Users\MTS\Desktop",
        r"C:\Users\MTS\Downloads",
        r"C:\Users\MTS\Documents",
        r"C:\Users\MTS\Pictures"

    ]

    for folder in folders:

        try:

            start_watcher(folder)

        except Exception as e:

            print(
                "WATCH ERROR:",
                folder,
                e
            )
    
@app.get("/")
def root():
    return {
        "message": "Reality Search Engine API",
        "status": "running"
    }