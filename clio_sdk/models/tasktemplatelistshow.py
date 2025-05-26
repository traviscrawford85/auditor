from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TasktemplatelistShowIn(BaseModel):
    data: Tasktemplatelist

class TasktemplatelistShowOut(BaseModel):
    data: Tasktemplatelist

class TasktemplatelistShowUpdate(BaseModel):
    data: Tasktemplatelist

class TasktemplatelistShowDb(BaseModel):
    data: Tasktemplatelist

