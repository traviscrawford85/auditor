from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CustomfieldsetListIn(BaseModel):
    data: List[Any]

class CustomfieldsetListOut(BaseModel):
    data: List[Any]

class CustomfieldsetListUpdate(BaseModel):
    data: List[Any]

class CustomfieldsetListDb(BaseModel):
    data: List[Any]

