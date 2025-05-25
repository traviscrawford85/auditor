from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class NoteListIn(BaseModel):
    data: List[Any]

class NoteListOut(BaseModel):
    data: List[Any]

class NoteListUpdate(BaseModel):
    data: List[Any]

class NoteListDb(BaseModel):
    data: List[Any]

