from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TasktemplatelistListIn(BaseModel):
    data: List[Tasktemplatelist]

class TasktemplatelistListOut(BaseModel):
    data: List[Tasktemplatelist]

class TasktemplatelistListUpdate(BaseModel):
    data: List[Tasktemplatelist]

class TasktemplatelistListDb(BaseModel):
    data: List[Tasktemplatelist]

