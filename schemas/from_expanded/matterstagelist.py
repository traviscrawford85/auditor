from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MatterstageListIn(BaseModel):
    data: List[Any]

class MatterstageListOut(BaseModel):
    data: List[Any]

class MatterstageListUpdate(BaseModel):
    data: List[Any]

class MatterstageListDb(BaseModel):
    data: List[Any]

