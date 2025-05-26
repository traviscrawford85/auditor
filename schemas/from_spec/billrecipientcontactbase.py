from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillrecipientcontactBaseIn(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    type: Optional[str] = None
    primary_email_address: Optional[str] = None

class BillrecipientcontactBaseOut(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    type: Optional[str] = None
    primary_email_address: Optional[str] = None

class BillrecipientcontactBaseUpdate(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    type: Optional[str] = None
    primary_email_address: Optional[str] = None

class BillrecipientcontactBaseDb(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    type: Optional[str] = None
    primary_email_address: Optional[str] = None

