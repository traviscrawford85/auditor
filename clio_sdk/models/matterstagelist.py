from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MatterstageListIn(BaseModel):
    data: List[Matterstage]

class MatterstageListOut(BaseModel):
    data: List[Matterstage]

class MatterstageListUpdate(BaseModel):
    data: List[Matterstage]

class MatterstageListDb(BaseModel):
    data: List[Matterstage]

