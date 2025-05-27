from typing import List

from pydantic import BaseModel

from .practicearea import PracticeareaOut


class PracticeareaListIn(BaseModel):
    data: List[PracticeareaIn]

class PracticeareaListOut(BaseModel):
    data: List[PracticeareaOut]

class PracticeareaListUpdate(BaseModel):
    data: List[PracticeareaUpdate]

class PracticeareaListDb(BaseModel):
    data: List[PracticeareaDb]

