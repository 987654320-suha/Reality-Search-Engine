from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.routes.memory_routes import router as memory_router
from app.routes.upload_routes import router as upload_router
from app.routes.search_routes import router as search_router
from app.routes.timeline_routes import router as timeline_router

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

app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads"
)

@app.get("/")
def root():
    return {
        "message": "Reality Search Engine API",
        "status": "running"
    }