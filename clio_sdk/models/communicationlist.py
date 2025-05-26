from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CommunicationListIn(BaseModel):
    data: List[Communication]

class CommunicationListOut(BaseModel):
    data: List[Communication]

class CommunicationListUpdate(BaseModel):
    data: List[Communication]

class CommunicationListDb(BaseModel):
    data: List[Communication]

