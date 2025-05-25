from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ContactcreaterequestdataphonenumbersinnerIn(BaseModel):
    name: Optional[str] = None
    number: Optional[str] = None
    default_number: Optional[str] = None

class ContactcreaterequestdataphonenumbersinnerOut(BaseModel):
    name: Optional[str] = None
    number: Optional[str] = None
    default_number: Optional[str] = None

class ContactcreaterequestdataphonenumbersinnerUpdate(BaseModel):
    name: Optional[str] = None
    number: Optional[str] = None
    default_number: Optional[str] = None

class ContactcreaterequestdataphonenumbersinnerDb(BaseModel):
    name: Optional[str] = None
    number: Optional[str] = None
    default_number: Optional[str] = None

