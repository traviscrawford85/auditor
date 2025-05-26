from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ExternalpropertyBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ExternalpropertyBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ExternalpropertyBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ExternalpropertyBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

