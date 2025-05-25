from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillrecipientContactBaseIn(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    type: Optional[str] = None
    primary_email_address: Optional[str] = None

class BillrecipientContactBaseOut(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    type: Optional[str] = None
    primary_email_address: Optional[str] = None

class BillrecipientContactBaseUpdate(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    type: Optional[str] = None
    primary_email_address: Optional[str] = None

class BillrecipientContactBaseDb(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    type: Optional[str] = None
    primary_email_address: Optional[str] = None

