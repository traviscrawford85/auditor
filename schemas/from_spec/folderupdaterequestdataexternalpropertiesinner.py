from typing import Optional

from pydantic import BaseModel


class FolderupdaterequestdataexternalpropertiesinnerIn(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    _destroy: Optional[str] = None

class FolderupdaterequestdataexternalpropertiesinnerOut(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    _destroy: Optional[str] = None

class FolderupdaterequestdataexternalpropertiesinnerUpdate(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    _destroy: Optional[str] = None

class FolderupdaterequestdataexternalpropertiesinnerDb(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    _destroy: Optional[str] = None

