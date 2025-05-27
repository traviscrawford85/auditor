from typing import Optional

from pydantic import BaseModel


class FoldercreaterequestdataexternalpropertiesinnerIn(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

class FoldercreaterequestdataexternalpropertiesinnerOut(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

class FoldercreaterequestdataexternalpropertiesinnerUpdate(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

class FoldercreaterequestdataexternalpropertiesinnerDb(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

