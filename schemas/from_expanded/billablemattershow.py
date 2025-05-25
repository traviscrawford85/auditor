from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillablematterShowIn(BaseModel):
    data: Any

class BillablematterShowOut(BaseModel):
    data: Any

class BillablematterShowUpdate(BaseModel):
    data: Any

class BillablematterShowDb(BaseModel):
    data: Any

