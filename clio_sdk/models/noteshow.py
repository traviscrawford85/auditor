from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class NoteShowIn(BaseModel):
    data: Note

class NoteShowOut(BaseModel):
    data: Note

class NoteShowUpdate(BaseModel):
    data: Note

class NoteShowDb(BaseModel):
    data: Note

