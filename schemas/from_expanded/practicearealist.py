from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PracticeareaListIn(BaseModel):
    data: List[Any]

class PracticeareaListOut(BaseModel):
    data: List[Any]

class PracticeareaListUpdate(BaseModel):
    data: List[Any]

class PracticeareaListDb(BaseModel):
    data: List[Any]

