from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ItemListIn(BaseModel):
    data: List[Any]

class ItemListOut(BaseModel):
    data: List[Any]

class ItemListUpdate(BaseModel):
    data: List[Any]

class ItemListDb(BaseModel):
    data: List[Any]

