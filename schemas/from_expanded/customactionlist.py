from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CustomactionListIn(BaseModel):
    data: List[Any]

class CustomactionListOut(BaseModel):
    data: List[Any]

class CustomactionListUpdate(BaseModel):
    data: List[Any]

class CustomactionListDb(BaseModel):
    data: List[Any]

