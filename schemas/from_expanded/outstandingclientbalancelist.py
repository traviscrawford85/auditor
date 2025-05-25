from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class OutstandingclientbalanceListIn(BaseModel):
    data: List[Any]

class OutstandingclientbalanceListOut(BaseModel):
    data: List[Any]

class OutstandingclientbalanceListUpdate(BaseModel):
    data: List[Any]

class OutstandingclientbalanceListDb(BaseModel):
    data: List[Any]

