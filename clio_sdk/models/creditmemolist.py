from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CreditmemoListIn(BaseModel):
    data: List[Creditmemo]

class CreditmemoListOut(BaseModel):
    data: List[Creditmemo]

class CreditmemoListUpdate(BaseModel):
    data: List[Creditmemo]

class CreditmemoListDb(BaseModel):
    data: List[Creditmemo]

