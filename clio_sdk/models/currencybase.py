from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CurrencyBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    code: Optional[str] = None
    sign: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class CurrencyBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    code: Optional[str] = None
    sign: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class CurrencyBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    code: Optional[str] = None
    sign: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class CurrencyBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    code: Optional[str] = None
    sign: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

