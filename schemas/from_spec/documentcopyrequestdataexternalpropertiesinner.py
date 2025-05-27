from typing import Optional

from pydantic import BaseModel


class DocumentcopyrequestdataexternalpropertiesinnerIn(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    _destroy: Optional[str] = None

class DocumentcopyrequestdataexternalpropertiesinnerOut(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    _destroy: Optional[str] = None

class DocumentcopyrequestdataexternalpropertiesinnerUpdate(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    _destroy: Optional[str] = None

class DocumentcopyrequestdataexternalpropertiesinnerDb(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    _destroy: Optional[str] = None

