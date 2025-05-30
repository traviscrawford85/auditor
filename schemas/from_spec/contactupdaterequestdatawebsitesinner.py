from typing import Optional

from pydantic import BaseModel


class ContactupdaterequestdatawebsitesinnerIn(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    id: Optional[str] = None
    default_web_site: Optional[str] = None
    _destroy: Optional[str] = None

class ContactupdaterequestdatawebsitesinnerOut(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    id: Optional[str] = None
    default_web_site: Optional[str] = None
    _destroy: Optional[str] = None

class ContactupdaterequestdatawebsitesinnerUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    id: Optional[str] = None
    default_web_site: Optional[str] = None
    _destroy: Optional[str] = None

class ContactupdaterequestdatawebsitesinnerDb(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    id: Optional[str] = None
    default_web_site: Optional[str] = None
    _destroy: Optional[str] = None

