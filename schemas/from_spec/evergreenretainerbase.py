from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class EvergreenretainerBaseIn(BaseModel):
    id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    etag: Optional[str] = None
    minimum_threshold: Optional[str] = None

class EvergreenretainerBaseOut(BaseModel):
    id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    etag: Optional[str] = None
    minimum_threshold: Optional[str] = None

class EvergreenretainerBaseUpdate(BaseModel):
    id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    etag: Optional[str] = None
    minimum_threshold: Optional[str] = None

class EvergreenretainerBaseDb(BaseModel):
    id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    etag: Optional[str] = None
    minimum_threshold: Optional[str] = None

