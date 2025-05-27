
from pydantic import BaseModel

from .practicearea import PracticeareaOut


class PracticeareaShowIn(BaseModel):
    data: PracticeareaIn

class PracticeareaShowOut(BaseModel):
    data: PracticeareaOut

class PracticeareaShowUpdate(BaseModel):
    data: PracticeareaUpdate

class PracticeareaShowDb(BaseModel):
    data: PracticeareaDb

