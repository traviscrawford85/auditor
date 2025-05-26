from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DamageListIn(BaseModel):
    data: List[Damage]

class DamageListOut(BaseModel):
    data: List[Damage]

class DamageListUpdate(BaseModel):
    data: List[Damage]

class DamageListDb(BaseModel):
    data: List[Damage]

