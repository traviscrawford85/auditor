from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ExternalpropertybaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ExternalpropertybaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ExternalpropertybaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ExternalpropertybaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

