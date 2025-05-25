from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillrecipientcontactbaseIn(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    type: Optional[str] = None
    primary_email_address: Optional[str] = None

class BillrecipientcontactbaseOut(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    type: Optional[str] = None
    primary_email_address: Optional[str] = None

class BillrecipientcontactbaseUpdate(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    type: Optional[str] = None
    primary_email_address: Optional[str] = None

class BillrecipientcontactbaseDb(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    type: Optional[str] = None
    primary_email_address: Optional[str] = None

