from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class GroupcreaterequestdataIn(BaseModel):
    name: Optional[str] = None

class GroupcreaterequestdataOut(BaseModel):
    name: Optional[str] = None

class GroupcreaterequestdataUpdate(BaseModel):
    name: Optional[str] = None

class GroupcreaterequestdataDb(BaseModel):
    name: Optional[str] = None

