from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ExpensecategoryListIn(BaseModel):
    data: List[Any]

class ExpensecategoryListOut(BaseModel):
    data: List[Any]

class ExpensecategoryListUpdate(BaseModel):
    data: List[Any]

class ExpensecategoryListDb(BaseModel):
    data: List[Any]

