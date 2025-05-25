from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TrustlineitemListIn(BaseModel):
    data: List[Any]

class TrustlineitemListOut(BaseModel):
    data: List[Any]

class TrustlineitemListUpdate(BaseModel):
    data: List[Any]

class TrustlineitemListDb(BaseModel):
    data: List[Any]

