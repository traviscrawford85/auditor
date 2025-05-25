from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MatterListIn(BaseModel):
    data: List[Any]

class MatterListOut(BaseModel):
    data: List[Any]

class MatterListUpdate(BaseModel):
    data: List[Any]

class MatterListDb(BaseModel):
    data: List[Any]

