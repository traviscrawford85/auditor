from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class AccountBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    state: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class AccountBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    state: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class AccountBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    state: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class AccountBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    state: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

