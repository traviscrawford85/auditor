from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class JurisdictionstotriggerListIn(BaseModel):
    data: List[Any]

class JurisdictionstotriggerListOut(BaseModel):
    data: List[Any]

class JurisdictionstotriggerListUpdate(BaseModel):
    data: List[Any]

class JurisdictionstotriggerListDb(BaseModel):
    data: List[Any]

