from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillthemebaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    account_id: Optional[str] = None
    default: Optional[str] = None
    name: Optional[str] = None
    config: Optional[str] = None

class BillthemebaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    account_id: Optional[str] = None
    default: Optional[str] = None
    name: Optional[str] = None
    config: Optional[str] = None

class BillthemebaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    account_id: Optional[str] = None
    default: Optional[str] = None
    name: Optional[str] = None
    config: Optional[str] = None

class BillthemebaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    account_id: Optional[str] = None
    default: Optional[str] = None
    name: Optional[str] = None
    config: Optional[str] = None

