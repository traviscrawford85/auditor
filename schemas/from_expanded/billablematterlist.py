from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillablematterListIn(BaseModel):
    data: List[Any]

class BillablematterListOut(BaseModel):
    data: List[Any]

class BillablematterListUpdate(BaseModel):
    data: List[Any]

class BillablematterListDb(BaseModel):
    data: List[Any]

