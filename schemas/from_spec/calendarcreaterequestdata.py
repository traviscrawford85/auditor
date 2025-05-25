from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

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

