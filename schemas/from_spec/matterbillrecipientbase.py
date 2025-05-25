from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MatterbillrecipientbaseIn(BaseModel):
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    updated_at: Optional[str] = None

class MatterbillrecipientbaseOut(BaseModel):
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    updated_at: Optional[str] = None

class MatterbillrecipientbaseUpdate(BaseModel):
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    updated_at: Optional[str] = None

class MatterbillrecipientbaseDb(BaseModel):
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    updated_at: Optional[str] = None

