from typing import Optional

from pydantic import BaseModel


class CalendarcreaterequestdataIn(BaseModel):
    color: Optional[str] = None
    name: str
    source: Optional[str] = None
    visible: Optional[str] = None

class CalendarcreaterequestdataOut(BaseModel):
    color: Optional[str] = None
    name: str
    source: Optional[str] = None
    visible: Optional[str] = None

class CalendarcreaterequestdataUpdate(BaseModel):
    color: Optional[str] = None
    name: str
    source: Optional[str] = None
    visible: Optional[str] = None

class CalendarcreaterequestdataDb(BaseModel):
    color: Optional[str] = None
    name: str
    source: Optional[str] = None
    visible: Optional[str] = None

