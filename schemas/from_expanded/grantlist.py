from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class GrantListIn(BaseModel):
    data: List[Any]

class GrantListOut(BaseModel):
    data: List[Any]

class GrantListUpdate(BaseModel):
    data: List[Any]

class GrantListDb(BaseModel):
    data: List[Any]

