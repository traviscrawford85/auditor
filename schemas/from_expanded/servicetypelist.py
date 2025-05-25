from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ServicetypeListIn(BaseModel):
    data: List[Any]

class ServicetypeListOut(BaseModel):
    data: List[Any]

class ServicetypeListUpdate(BaseModel):
    data: List[Any]

class ServicetypeListDb(BaseModel):
    data: List[Any]

