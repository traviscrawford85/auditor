from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class OutstandingclientbalanceListIn(BaseModel):
    data: List[Outstandingclientbalance]

class OutstandingclientbalanceListOut(BaseModel):
    data: List[Outstandingclientbalance]

class OutstandingclientbalanceListUpdate(BaseModel):
    data: List[Outstandingclientbalance]

class OutstandingclientbalanceListDb(BaseModel):
    data: List[Outstandingclientbalance]

