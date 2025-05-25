from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillListIn(BaseModel):
    data: List[Any]

class BillListOut(BaseModel):
    data: List[Any]

class BillListUpdate(BaseModel):
    data: List[Any]

class BillListDb(BaseModel):
    data: List[Any]

