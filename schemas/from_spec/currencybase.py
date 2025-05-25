from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CurrencybaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    code: Optional[str] = None
    sign: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CurrencybaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    code: Optional[str] = None
    sign: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CurrencybaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    code: Optional[str] = None
    sign: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CurrencybaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    code: Optional[str] = None
    sign: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

