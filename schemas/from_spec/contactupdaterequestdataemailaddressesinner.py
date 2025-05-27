from typing import Optional

from pydantic import BaseModel


class ContactupdaterequestdataemailaddressesinnerIn(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    address: Optional[str] = None
    default_email: Optional[str] = None
    _destroy: Optional[str] = None

class ContactupdaterequestdataemailaddressesinnerOut(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    address: Optional[str] = None
    default_email: Optional[str] = None
    _destroy: Optional[str] = None

class ContactupdaterequestdataemailaddressesinnerUpdate(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    address: Optional[str] = None
    default_email: Optional[str] = None
    _destroy: Optional[str] = None

class ContactupdaterequestdataemailaddressesinnerDb(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    address: Optional[str] = None
    default_email: Optional[str] = None
    _destroy: Optional[str] = None

