from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LaukexpensecategoryListIn(BaseModel):
    data: List[Any]

class LaukexpensecategoryListOut(BaseModel):
    data: List[Any]

class LaukexpensecategoryListUpdate(BaseModel):
    data: List[Any]

class LaukexpensecategoryListDb(BaseModel):
    data: List[Any]

