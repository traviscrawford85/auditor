from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillthemeBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    account_id: Optional[int] = None
    default: Optional[bool] = None
    name: Optional[str] = None
    config: Optional[str] = None

class BillthemeBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    account_id: Optional[int] = None
    default: Optional[bool] = None
    name: Optional[str] = None
    config: Optional[str] = None

class BillthemeBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    account_id: Optional[int] = None
    default: Optional[bool] = None
    name: Optional[str] = None
    config: Optional[str] = None

class BillthemeBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    account_id: Optional[int] = None
    default: Optional[bool] = None
    name: Optional[str] = None
    config: Optional[str] = None

