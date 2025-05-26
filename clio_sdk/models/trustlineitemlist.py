from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TrustlineitemListIn(BaseModel):
    data: List[Trustlineitem]

class TrustlineitemListOut(BaseModel):
    data: List[Trustlineitem]

class TrustlineitemListUpdate(BaseModel):
    data: List[Trustlineitem]

class TrustlineitemListDb(BaseModel):
    data: List[Trustlineitem]

