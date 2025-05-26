from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MyeventListIn(BaseModel):
    data: List[Myevent]

class MyeventListOut(BaseModel):
    data: List[Myevent]

class MyeventListUpdate(BaseModel):
    data: List[Myevent]

class MyeventListDb(BaseModel):
    data: List[Myevent]

