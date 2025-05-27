from typing import Optional

from pydantic import BaseModel


class WebhookcreaterequestdataIn(BaseModel):
    events: Optional[str] = None
    expires_at: Optional[str] = None
    fields: str
    model: str
    url: str

class WebhookcreaterequestdataOut(BaseModel):
    events: Optional[str] = None
    expires_at: Optional[str] = None
    fields: str
    model: str
    url: str

class WebhookcreaterequestdataUpdate(BaseModel):
    events: Optional[str] = None
    expires_at: Optional[str] = None
    fields: str
    model: str
    url: str

class WebhookcreaterequestdataDb(BaseModel):
    events: Optional[str] = None
    expires_at: Optional[str] = None
    fields: str
    model: str
    url: str

