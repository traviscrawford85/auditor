from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillthemeListIn(BaseModel):
    data: List[Any]

class BillthemeListOut(BaseModel):
    data: List[Any]

class BillthemeListUpdate(BaseModel):
    data: List[Any]

class BillthemeListDb(BaseModel):
    data: List[Any]

