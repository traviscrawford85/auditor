from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class JurisdictionstotriggerListIn(BaseModel):
    data: List[Jurisdictionstotrigger]

class JurisdictionstotriggerListOut(BaseModel):
    data: List[Jurisdictionstotrigger]

class JurisdictionstotriggerListUpdate(BaseModel):
    data: List[Jurisdictionstotrigger]

class JurisdictionstotriggerListDb(BaseModel):
    data: List[Jurisdictionstotrigger]

