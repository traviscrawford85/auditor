from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class GrantListIn(BaseModel):
    data: List[Grant]

class GrantListOut(BaseModel):
    data: List[Grant]

class GrantListUpdate(BaseModel):
    data: List[Grant]

class GrantListDb(BaseModel):
    data: List[Grant]

