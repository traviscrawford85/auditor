from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class EmailaddressbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class EmailaddressbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class EmailaddressbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class EmailaddressbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

