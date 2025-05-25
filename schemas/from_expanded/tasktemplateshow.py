from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TasktemplateShowIn(BaseModel):
    data: Any

class TasktemplateShowOut(BaseModel):
    data: Any

class TasktemplateShowUpdate(BaseModel):
    data: Any

class TasktemplateShowDb(BaseModel):
    data: Any

