from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class NoteListIn(BaseModel):
    data: List[Note]

class NoteListOut(BaseModel):
    data: List[Note]

class NoteListUpdate(BaseModel):
    data: List[Note]

class NoteListDb(BaseModel):
    data: List[Note]

