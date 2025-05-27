
from pydantic import BaseModel

from .jurisdictionstotrigger import JurisdictionstotriggerOut


class JurisdictionstotriggerShowIn(BaseModel):
    data: JurisdictionstotriggerIn

class JurisdictionstotriggerShowOut(BaseModel):
    data: JurisdictionstotriggerOut

class JurisdictionstotriggerShowUpdate(BaseModel):
    data: JurisdictionstotriggerUpdate

class JurisdictionstotriggerShowDb(BaseModel):
    data: JurisdictionstotriggerDb

