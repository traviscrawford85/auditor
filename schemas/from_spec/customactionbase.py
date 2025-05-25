from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CustomactionbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    label: Optional[str] = None
    target_url: Optional[str] = None
    ui_reference: Optional[str] = None

class CustomactionbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    label: Optional[str] = None
    target_url: Optional[str] = None
    ui_reference: Optional[str] = None

class CustomactionbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    label: Optional[str] = None
    target_url: Optional[str] = None
    ui_reference: Optional[str] = None

class CustomactionbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    label: Optional[str] = None
    target_url: Optional[str] = None
    ui_reference: Optional[str] = None

