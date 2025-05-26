from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillablematterListIn(BaseModel):
    data: List[Billablematter]

class BillablematterListOut(BaseModel):
    data: List[Billablematter]

class BillablematterListUpdate(BaseModel):
    data: List[Billablematter]

class BillablematterListDb(BaseModel):
    data: List[Billablematter]

