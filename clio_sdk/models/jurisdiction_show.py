
from pydantic import BaseModel

from .jurisdiction import JurisdictionOut


class JurisdictionShowIn(BaseModel):
    data: JurisdictionIn

class JurisdictionShowOut(BaseModel):
    data: JurisdictionOut

class JurisdictionShowUpdate(BaseModel):
    data: JurisdictionUpdate

class JurisdictionShowDb(BaseModel):
    data: JurisdictionDb

