from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ServicetypeListIn(BaseModel):
    data: List[Servicetype]

class ServicetypeListOut(BaseModel):
    data: List[Servicetype]

class ServicetypeListUpdate(BaseModel):
    data: List[Servicetype]

class ServicetypeListDb(BaseModel):
    data: List[Servicetype]

