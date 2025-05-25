from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CustomfieldsetbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    parent_type: Optional[str] = None
    displayed: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CustomfieldsetbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    parent_type: Optional[str] = None
    displayed: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CustomfieldsetbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    parent_type: Optional[str] = None
    displayed: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CustomfieldsetbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    parent_type: Optional[str] = None
    displayed: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

