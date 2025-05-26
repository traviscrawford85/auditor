from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class InstantmessengerBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class InstantmessengerBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class InstantmessengerBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class InstantmessengerBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

