from typing import Optional

from pydantic import BaseModel


class ContactcreaterequestdatawebsitesinnerIn(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    default_web_site: Optional[str] = None

class ContactcreaterequestdatawebsitesinnerOut(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    default_web_site: Optional[str] = None

class ContactcreaterequestdatawebsitesinnerUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    default_web_site: Optional[str] = None

class ContactcreaterequestdatawebsitesinnerDb(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    default_web_site: Optional[str] = None

