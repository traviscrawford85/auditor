from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class UtbmssetListIn(BaseModel):
    data: List[Any]

class UtbmssetListOut(BaseModel):
    data: List[Any]

class UtbmssetListUpdate(BaseModel):
    data: List[Any]

class UtbmssetListDb(BaseModel):
    data: List[Any]

