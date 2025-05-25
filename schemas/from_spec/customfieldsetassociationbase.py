from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CustomfieldsetassociationbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    display_order: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CustomfieldsetassociationbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    display_order: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CustomfieldsetassociationbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    display_order: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CustomfieldsetassociationbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    display_order: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

