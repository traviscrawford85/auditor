from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BanktransferBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    amount: Optional[float] = None
    date: Optional[datetime] = None
    description: Optional[str] = None
    primary_authorizer: Optional[str] = None
    secondary_authorizer: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class BanktransferBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    amount: Optional[float] = None
    date: Optional[datetime] = None
    description: Optional[str] = None
    primary_authorizer: Optional[str] = None
    secondary_authorizer: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class BanktransferBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    amount: Optional[float] = None
    date: Optional[datetime] = None
    description: Optional[str] = None
    primary_authorizer: Optional[str] = None
    secondary_authorizer: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class BanktransferBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    amount: Optional[float] = None
    date: Optional[datetime] = None
    description: Optional[str] = None
    primary_authorizer: Optional[str] = None
    secondary_authorizer: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

