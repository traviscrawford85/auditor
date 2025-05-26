from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillShowIn(BaseModel):
    data: Bill

class BillShowOut(BaseModel):
    data: Bill

class BillShowUpdate(BaseModel):
    data: Bill

class BillShowDb(BaseModel):
    data: Bill

