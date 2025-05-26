from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TasktemplateShowIn(BaseModel):
    data: Tasktemplate

class TasktemplateShowOut(BaseModel):
    data: Tasktemplate

class TasktemplateShowUpdate(BaseModel):
    data: Tasktemplate

class TasktemplateShowDb(BaseModel):
    data: Tasktemplate

