from typing import Optional

from pydantic import BaseModel


class CommunicationcreaterequestdataexternalpropertiesinnerIn(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

class CommunicationcreaterequestdataexternalpropertiesinnerOut(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

class CommunicationcreaterequestdataexternalpropertiesinnerUpdate(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

class CommunicationcreaterequestdataexternalpropertiesinnerDb(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

