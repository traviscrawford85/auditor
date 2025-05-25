from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class EvergreenretainerbaseIn(BaseModel):
    id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    etag: Optional[str] = None
    minimum_threshold: Optional[str] = None

class EvergreenretainerbaseOut(BaseModel):
    id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    etag: Optional[str] = None
    minimum_threshold: Optional[str] = None

class EvergreenretainerbaseUpdate(BaseModel):
    id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    etag: Optional[str] = None
    minimum_threshold: Optional[str] = None

class EvergreenretainerbaseDb(BaseModel):
    id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    etag: Optional[str] = None
    minimum_threshold: Optional[str] = None

