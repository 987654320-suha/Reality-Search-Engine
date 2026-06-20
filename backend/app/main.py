from fastapi import FastAPI

from app.routes.memory_routes import router as memory_router
from app.routes.upload_routes import router as upload_router

app = FastAPI(
    title="Reality Search Engine",
    version="1.0.0"
)

app.include_router(memory_router)
app.include_router(upload_router)

@app.get("/")
def root():
    return {
        "message": "Reality Search Engine API",
        "status": "running"
    }