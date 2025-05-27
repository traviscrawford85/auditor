from typing import Optional

from pydantic import BaseModel


class ContactcreaterequestdataavatarIn(BaseModel):
    image: Optional[str] = None
    _destroy: Optional[str] = None

class ContactcreaterequestdataavatarOut(BaseModel):
    image: Optional[str] = None
    _destroy: Optional[str] = None

class ContactcreaterequestdataavatarUpdate(BaseModel):
    image: Optional[str] = None
    _destroy: Optional[str] = None

class ContactcreaterequestdataavatarDb(BaseModel):
    image: Optional[str] = None
    _destroy: Optional[str] = None

