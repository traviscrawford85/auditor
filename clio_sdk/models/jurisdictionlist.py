from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class JurisdictionListIn(BaseModel):
    data: List[Jurisdiction]

class JurisdictionListOut(BaseModel):
    data: List[Jurisdiction]

class JurisdictionListUpdate(BaseModel):
    data: List[Jurisdiction]

class JurisdictionListDb(BaseModel):
    data: List[Jurisdiction]

