from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillingsettingShowIn(BaseModel):
    data: Any

class BillingsettingShowOut(BaseModel):
    data: Any

class BillingsettingShowUpdate(BaseModel):
    data: Any

class BillingsettingShowDb(BaseModel):
    data: Any

