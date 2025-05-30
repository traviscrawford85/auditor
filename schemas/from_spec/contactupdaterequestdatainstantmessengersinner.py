from typing import Optional

from pydantic import BaseModel


class ContactupdaterequestdatainstantmessengersinnerIn(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    id: Optional[str] = None
    _destroy: Optional[str] = None

class ContactupdaterequestdatainstantmessengersinnerOut(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    id: Optional[str] = None
    _destroy: Optional[str] = None

class ContactupdaterequestdatainstantmessengersinnerUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    id: Optional[str] = None
    _destroy: Optional[str] = None

class ContactupdaterequestdatainstantmessengersinnerDb(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    id: Optional[str] = None
    _destroy: Optional[str] = None

