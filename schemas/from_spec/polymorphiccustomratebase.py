from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PolymorphiccustomratebaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    rate: Optional[str] = None
    award: Optional[str] = None
    note: Optional[str] = None
    date: Optional[str] = None

class PolymorphiccustomratebaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    rate: Optional[str] = None
    award: Optional[str] = None
    note: Optional[str] = None
    date: Optional[str] = None

class PolymorphiccustomratebaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    rate: Optional[str] = None
    award: Optional[str] = None
    note: Optional[str] = None
    date: Optional[str] = None

class PolymorphiccustomratebaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    rate: Optional[str] = None
    award: Optional[str] = None
    note: Optional[str] = None
    date: Optional[str] = None

