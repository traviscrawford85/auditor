from typing import Optional

from pydantic import BaseModel


class WebhookupdaterequestdataIn(BaseModel):
    events: Optional[str] = None
    expires_at: Optional[str] = None
    fields: Optional[str] = None
    model: Optional[str] = None
    url: Optional[str] = None

class WebhookupdaterequestdataOut(BaseModel):
    events: Optional[str] = None
    expires_at: Optional[str] = None
    fields: Optional[str] = None
    model: Optional[str] = None
    url: Optional[str] = None

class WebhookupdaterequestdataUpdate(BaseModel):
    events: Optional[str] = None
    expires_at: Optional[str] = None
    fields: Optional[str] = None
    model: Optional[str] = None
    url: Optional[str] = None

class WebhookupdaterequestdataDb(BaseModel):
    events: Optional[str] = None
    expires_at: Optional[str] = None
    fields: Optional[str] = None
    model: Optional[str] = None
    url: Optional[str] = None

