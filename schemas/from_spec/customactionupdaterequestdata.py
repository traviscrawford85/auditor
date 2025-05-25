from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CustomactionupdaterequestdataIn(BaseModel):
    label: Optional[str] = None
    target_url: Optional[str] = None
    ui_reference: Optional[str] = None

class CustomactionupdaterequestdataOut(BaseModel):
    label: Optional[str] = None
    target_url: Optional[str] = None
    ui_reference: Optional[str] = None

class CustomactionupdaterequestdataUpdate(BaseModel):
    label: Optional[str] = None
    target_url: Optional[str] = None
    ui_reference: Optional[str] = None

class CustomactionupdaterequestdataDb(BaseModel):
    label: Optional[str] = None
    target_url: Optional[str] = None
    ui_reference: Optional[str] = None

