from typing import Optional

from pydantic import BaseModel


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

