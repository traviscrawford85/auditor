from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class UtbmssetbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class UtbmssetbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class UtbmssetbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class UtbmssetbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

