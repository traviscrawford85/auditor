from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TasktemplatelistListIn(BaseModel):
    data: List[Any]

class TasktemplatelistListOut(BaseModel):
    data: List[Any]

class TasktemplatelistListUpdate(BaseModel):
    data: List[Any]

class TasktemplatelistListDb(BaseModel):
    data: List[Any]

