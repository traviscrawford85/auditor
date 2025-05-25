from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TasktemplateListIn(BaseModel):
    data: List[Any]

class TasktemplateListOut(BaseModel):
    data: List[Any]

class TasktemplateListUpdate(BaseModel):
    data: List[Any]

class TasktemplateListDb(BaseModel):
    data: List[Any]

