from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CommunicationListIn(BaseModel):
    data: List[Any]

class CommunicationListOut(BaseModel):
    data: List[Any]

class CommunicationListUpdate(BaseModel):
    data: List[Any]

class CommunicationListDb(BaseModel):
    data: List[Any]

