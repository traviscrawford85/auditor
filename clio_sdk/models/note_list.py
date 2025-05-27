from typing import List

from pydantic import BaseModel

from .note import NoteOut


class NoteListIn(BaseModel):
    data: List[NoteIn]

class NoteListOut(BaseModel):
    data: List[NoteOut]

class NoteListUpdate(BaseModel):
    data: List[NoteUpdate]

class NoteListDb(BaseModel):
    data: List[NoteDb]

