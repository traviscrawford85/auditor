from typing import Optional

from pydantic import BaseModel


class CommunicationupdaterequestdataexternalpropertiesinnerIn(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    _destroy: Optional[str] = None

class CommunicationupdaterequestdataexternalpropertiesinnerOut(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    _destroy: Optional[str] = None

class CommunicationupdaterequestdataexternalpropertiesinnerUpdate(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    _destroy: Optional[str] = None

class CommunicationupdaterequestdataexternalpropertiesinnerDb(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    _destroy: Optional[str] = None

