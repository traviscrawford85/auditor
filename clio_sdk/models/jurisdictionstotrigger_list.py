from typing import List

from pydantic import BaseModel

from .jurisdictionstotrigger import JurisdictionstotriggerOut


class JurisdictionstotriggerListIn(BaseModel):
    data: List[JurisdictionstotriggerIn]

class JurisdictionstotriggerListOut(BaseModel):
    data: List[JurisdictionstotriggerOut]

class JurisdictionstotriggerListUpdate(BaseModel):
    data: List[JurisdictionstotriggerUpdate]

class JurisdictionstotriggerListDb(BaseModel):
    data: List[JurisdictionstotriggerDb]

