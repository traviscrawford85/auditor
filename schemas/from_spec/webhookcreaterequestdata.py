from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

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

