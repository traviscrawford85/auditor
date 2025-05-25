from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MatterdocketListIn(BaseModel):
    data: List[Any]

class MatterdocketListOut(BaseModel):
    data: List[Any]

class MatterdocketListUpdate(BaseModel):
    data: List[Any]

class MatterdocketListDb(BaseModel):
    data: List[Any]

