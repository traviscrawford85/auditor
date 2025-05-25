from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillableclientListIn(BaseModel):
    data: List[Any]

class BillableclientListOut(BaseModel):
    data: List[Any]

class BillableclientListUpdate(BaseModel):
    data: List[Any]

class BillableclientListDb(BaseModel):
    data: List[Any]

