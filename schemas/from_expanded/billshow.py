from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillShowIn(BaseModel):
    data: Any

class BillShowOut(BaseModel):
    data: Any

class BillShowUpdate(BaseModel):
    data: Any

class BillShowDb(BaseModel):
    data: Any

