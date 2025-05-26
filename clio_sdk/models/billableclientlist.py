from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillableclientListIn(BaseModel):
    data: List[Billableclient]

class BillableclientListOut(BaseModel):
    data: List[Billableclient]

class BillableclientListUpdate(BaseModel):
    data: List[Billableclient]

class BillableclientListDb(BaseModel):
    data: List[Billableclient]

