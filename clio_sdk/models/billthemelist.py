from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillthemeListIn(BaseModel):
    data: List[Billtheme]

class BillthemeListOut(BaseModel):
    data: List[Billtheme]

class BillthemeListUpdate(BaseModel):
    data: List[Billtheme]

class BillthemeListDb(BaseModel):
    data: List[Billtheme]

