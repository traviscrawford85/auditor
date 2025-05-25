from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class EmailaddressListIn(BaseModel):
    data: List[Any]

class EmailaddressListOut(BaseModel):
    data: List[Any]

class EmailaddressListUpdate(BaseModel):
    data: List[Any]

class EmailaddressListDb(BaseModel):
    data: List[Any]

