from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class GroupListIn(BaseModel):
    data: List[Group]

class GroupListOut(BaseModel):
    data: List[Group]

class GroupListUpdate(BaseModel):
    data: List[Group]

class GroupListDb(BaseModel):
    data: List[Group]

