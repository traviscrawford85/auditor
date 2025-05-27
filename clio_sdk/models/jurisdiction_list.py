from typing import List

from pydantic import BaseModel

from .jurisdiction import JurisdictionOut


class JurisdictionListIn(BaseModel):
    data: List[JurisdictionIn]

class JurisdictionListOut(BaseModel):
    data: List[JurisdictionOut]

class JurisdictionListUpdate(BaseModel):
    data: List[JurisdictionUpdate]

class JurisdictionListDb(BaseModel):
    data: List[JurisdictionDb]

