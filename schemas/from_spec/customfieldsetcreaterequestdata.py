from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CustomfieldsetcreaterequestdataIn(BaseModel):
    displayed: Optional[str] = None
    name: str
    parent_type: Optional[str] = None

class CustomfieldsetcreaterequestdataOut(BaseModel):
    displayed: Optional[str] = None
    name: str
    parent_type: Optional[str] = None

class CustomfieldsetcreaterequestdataUpdate(BaseModel):
    displayed: Optional[str] = None
    name: str
    parent_type: Optional[str] = None

class CustomfieldsetcreaterequestdataDb(BaseModel):
    displayed: Optional[str] = None
    name: str
    parent_type: Optional[str] = None

