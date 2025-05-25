from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class GroupListIn(BaseModel):
    data: List[Any]

class GroupListOut(BaseModel):
    data: List[Any]

class GroupListUpdate(BaseModel):
    data: List[Any]

class GroupListDb(BaseModel):
    data: List[Any]

