from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MyeventListIn(BaseModel):
    data: List[Any]

class MyeventListOut(BaseModel):
    data: List[Any]

class MyeventListUpdate(BaseModel):
    data: List[Any]

class MyeventListDb(BaseModel):
    data: List[Any]

