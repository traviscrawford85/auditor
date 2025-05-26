from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TasktemplateListIn(BaseModel):
    data: List[Tasktemplate]

class TasktemplateListOut(BaseModel):
    data: List[Tasktemplate]

class TasktemplateListUpdate(BaseModel):
    data: List[Tasktemplate]

class TasktemplateListDb(BaseModel):
    data: List[Tasktemplate]

