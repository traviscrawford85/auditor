from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CustomfieldsetupdaterequestdataIn(BaseModel):
    displayed: Optional[str] = None
    name: Optional[str] = None
    parent_type: Optional[str] = None

class CustomfieldsetupdaterequestdataOut(BaseModel):
    displayed: Optional[str] = None
    name: Optional[str] = None
    parent_type: Optional[str] = None

class CustomfieldsetupdaterequestdataUpdate(BaseModel):
    displayed: Optional[str] = None
    name: Optional[str] = None
    parent_type: Optional[str] = None

class CustomfieldsetupdaterequestdataDb(BaseModel):
    displayed: Optional[str] = None
    name: Optional[str] = None
    parent_type: Optional[str] = None

