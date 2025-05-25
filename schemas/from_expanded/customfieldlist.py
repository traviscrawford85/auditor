from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CustomfieldListIn(BaseModel):
    data: List[Any]

class CustomfieldListOut(BaseModel):
    data: List[Any]

class CustomfieldListUpdate(BaseModel):
    data: List[Any]

class CustomfieldListDb(BaseModel):
    data: List[Any]

