from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DamageListIn(BaseModel):
    data: List[Any]

class DamageListOut(BaseModel):
    data: List[Any]

class DamageListUpdate(BaseModel):
    data: List[Any]

class DamageListDb(BaseModel):
    data: List[Any]

