from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class JurisdictionstotriggerShowIn(BaseModel):
    data: Jurisdictionstotrigger

class JurisdictionstotriggerShowOut(BaseModel):
    data: Jurisdictionstotrigger

class JurisdictionstotriggerShowUpdate(BaseModel):
    data: Jurisdictionstotrigger

class JurisdictionstotriggerShowDb(BaseModel):
    data: Jurisdictionstotrigger

