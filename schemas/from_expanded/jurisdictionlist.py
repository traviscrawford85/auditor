from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class JurisdictionListIn(BaseModel):
    data: List[Any]

class JurisdictionListOut(BaseModel):
    data: List[Any]

class JurisdictionListUpdate(BaseModel):
    data: List[Any]

class JurisdictionListDb(BaseModel):
    data: List[Any]

