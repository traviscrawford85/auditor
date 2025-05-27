from typing import Optional

from pydantic import BaseModel


class ActivityratecreaterequestdataIn(BaseModel):
    co_counsel_contact_id: Optional[str] = None
    contact_id: Optional[str] = None
    flat_rate: Optional[str] = None
    rate: Optional[str] = None

class ActivityratecreaterequestdataOut(BaseModel):
    co_counsel_contact_id: Optional[str] = None
    contact_id: Optional[str] = None
    flat_rate: Optional[str] = None
    rate: Optional[str] = None

class ActivityratecreaterequestdataUpdate(BaseModel):
    co_counsel_contact_id: Optional[str] = None
    contact_id: Optional[str] = None
    flat_rate: Optional[str] = None
    rate: Optional[str] = None

class ActivityratecreaterequestdataDb(BaseModel):
    co_counsel_contact_id: Optional[str] = None
    contact_id: Optional[str] = None
    flat_rate: Optional[str] = None
    rate: Optional[str] = None

