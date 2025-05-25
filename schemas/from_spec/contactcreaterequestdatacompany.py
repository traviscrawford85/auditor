from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ContactcreaterequestdatacompanyIn(BaseModel):
    id: Optional[str] = None

class ContactcreaterequestdatacompanyOut(BaseModel):
    id: Optional[str] = None

class ContactcreaterequestdatacompanyUpdate(BaseModel):
    id: Optional[str] = None

class ContactcreaterequestdatacompanyDb(BaseModel):
    id: Optional[str] = None

