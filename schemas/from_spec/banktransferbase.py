from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BanktransferbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    amount: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None
    primary_authorizer: Optional[str] = None
    secondary_authorizer: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class BanktransferbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    amount: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None
    primary_authorizer: Optional[str] = None
    secondary_authorizer: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class BanktransferbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    amount: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None
    primary_authorizer: Optional[str] = None
    secondary_authorizer: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class BanktransferbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    amount: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None
    primary_authorizer: Optional[str] = None
    secondary_authorizer: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

