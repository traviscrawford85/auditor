from typing import Optional

from pydantic import BaseModel


class ContactcreaterequestdatacompanyIn(BaseModel):
    id: Optional[str] = None

class ContactcreaterequestdatacompanyOut(BaseModel):
    id: Optional[str] = None

class ContactcreaterequestdatacompanyUpdate(BaseModel):
    id: Optional[str] = None

class ContactcreaterequestdatacompanyDb(BaseModel):
    id: Optional[str] = None

