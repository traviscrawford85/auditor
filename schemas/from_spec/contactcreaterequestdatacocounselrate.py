from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ContactcreaterequestdatacocounselrateIn(BaseModel):
    rate: Optional[str] = None

class ContactcreaterequestdatacocounselrateOut(BaseModel):
    rate: Optional[str] = None

class ContactcreaterequestdatacocounselrateUpdate(BaseModel):
    rate: Optional[str] = None

class ContactcreaterequestdatacocounselrateDb(BaseModel):
    rate: Optional[str] = None

