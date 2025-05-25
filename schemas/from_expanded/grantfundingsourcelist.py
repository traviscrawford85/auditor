from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class GrantfundingsourceListIn(BaseModel):
    data: List[Any]

class GrantfundingsourceListOut(BaseModel):
    data: List[Any]

class GrantfundingsourceListUpdate(BaseModel):
    data: List[Any]

class GrantfundingsourceListDb(BaseModel):
    data: List[Any]

