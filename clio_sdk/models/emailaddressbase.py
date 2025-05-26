from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class EmailaddressBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class EmailaddressBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class EmailaddressBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class EmailaddressBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

