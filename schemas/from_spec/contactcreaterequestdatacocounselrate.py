from typing import Optional

from pydantic import BaseModel


class ContactcreaterequestdatacocounselrateIn(BaseModel):
    rate: Optional[str] = None

class ContactcreaterequestdatacocounselrateOut(BaseModel):
    rate: Optional[str] = None

class ContactcreaterequestdatacocounselrateUpdate(BaseModel):
    rate: Optional[str] = None

class ContactcreaterequestdatacocounselrateDb(BaseModel):
    rate: Optional[str] = None

