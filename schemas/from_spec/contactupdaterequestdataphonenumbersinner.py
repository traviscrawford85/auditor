from typing import Optional

from pydantic import BaseModel


class ContactupdaterequestdataphonenumbersinnerIn(BaseModel):
    name: Optional[str] = None
    number: Optional[str] = None
    default_number: Optional[str] = None
    id: Optional[str] = None
    _destroy: Optional[str] = None

class ContactupdaterequestdataphonenumbersinnerOut(BaseModel):
    name: Optional[str] = None
    number: Optional[str] = None
    default_number: Optional[str] = None
    id: Optional[str] = None
    _destroy: Optional[str] = None

class ContactupdaterequestdataphonenumbersinnerUpdate(BaseModel):
    name: Optional[str] = None
    number: Optional[str] = None
    default_number: Optional[str] = None
    id: Optional[str] = None
    _destroy: Optional[str] = None

class ContactupdaterequestdataphonenumbersinnerDb(BaseModel):
    name: Optional[str] = None
    number: Optional[str] = None
    default_number: Optional[str] = None
    id: Optional[str] = None
    _destroy: Optional[str] = None

