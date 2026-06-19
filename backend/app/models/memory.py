from pydantic import BaseModel
from typing import Optional

class Memory(BaseModel):
    title: str
    description: str
    date: str
    location: Optional[str] = None