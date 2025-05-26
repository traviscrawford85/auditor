from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillListIn(BaseModel):
    data: List[Bill]

class BillListOut(BaseModel):
    data: List[Bill]

class BillListUpdate(BaseModel):
    data: List[Bill]

class BillListDb(BaseModel):
    data: List[Bill]

