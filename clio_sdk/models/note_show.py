
from pydantic import BaseModel

from .note import NoteOut


class NoteShowIn(BaseModel):
    data: NoteIn

class NoteShowOut(BaseModel):
    data: NoteOut

class NoteShowUpdate(BaseModel):
    data: NoteUpdate

class NoteShowDb(BaseModel):
    data: NoteDb

