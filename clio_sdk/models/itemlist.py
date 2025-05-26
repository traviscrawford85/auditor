from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ItemListIn(BaseModel):
    data: List[Item]

class ItemListOut(BaseModel):
    data: List[Item]

class ItemListUpdate(BaseModel):
    data: List[Item]

class ItemListDb(BaseModel):
    data: List[Item]

