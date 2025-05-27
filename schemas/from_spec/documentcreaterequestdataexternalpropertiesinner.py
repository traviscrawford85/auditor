from typing import Optional

from pydantic import BaseModel


class DocumentcreaterequestdataexternalpropertiesinnerIn(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

class DocumentcreaterequestdataexternalpropertiesinnerOut(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

class DocumentcreaterequestdataexternalpropertiesinnerUpdate(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

class DocumentcreaterequestdataexternalpropertiesinnerDb(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

