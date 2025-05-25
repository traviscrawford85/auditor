from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ContactcreaterequestdataemailaddressesinnerIn(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    default_email: Optional[str] = None

class ContactcreaterequestdataemailaddressesinnerOut(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    default_email: Optional[str] = None

class ContactcreaterequestdataemailaddressesinnerUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    default_email: Optional[str] = None

class ContactcreaterequestdataemailaddressesinnerDb(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    default_email: Optional[str] = None

