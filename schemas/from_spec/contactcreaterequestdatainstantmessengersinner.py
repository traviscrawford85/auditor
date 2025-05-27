from typing import Optional

from pydantic import BaseModel


class ContactcreaterequestdatainstantmessengersinnerIn(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None

class ContactcreaterequestdatainstantmessengersinnerOut(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None

class ContactcreaterequestdatainstantmessengersinnerUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None

class ContactcreaterequestdatainstantmessengersinnerDb(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None

