from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PracticeareaListIn(BaseModel):
    data: List[Practicearea]

class PracticeareaListOut(BaseModel):
    data: List[Practicearea]

class PracticeareaListUpdate(BaseModel):
    data: List[Practicearea]

class PracticeareaListDb(BaseModel):
    data: List[Practicearea]

