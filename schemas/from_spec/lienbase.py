from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LienbaseIn(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    lien_type: Optional[str] = None
    mark_as_lien: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class LienbaseOut(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    lien_type: Optional[str] = None
    mark_as_lien: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class LienbaseUpdate(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    lien_type: Optional[str] = None
    mark_as_lien: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class LienbaseDb(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    lien_type: Optional[str] = None
    mark_as_lien: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

