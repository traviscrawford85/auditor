from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class NoteShowIn(BaseModel):
    data: Any

class NoteShowOut(BaseModel):
    data: Any

class NoteShowUpdate(BaseModel):
    data: Any

class NoteShowDb(BaseModel):
    data: Any

