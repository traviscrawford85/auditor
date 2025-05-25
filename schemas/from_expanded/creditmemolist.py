from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CreditmemoListIn(BaseModel):
    data: List[Any]

class CreditmemoListOut(BaseModel):
    data: List[Any]

class CreditmemoListUpdate(BaseModel):
    data: List[Any]

class CreditmemoListDb(BaseModel):
    data: List[Any]

