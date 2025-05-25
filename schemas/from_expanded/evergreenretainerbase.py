from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class EvergreenretainerBaseIn(BaseModel):
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    etag: Optional[str] = None
    minimum_threshold: Optional[float] = None

class EvergreenretainerBaseOut(BaseModel):
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    etag: Optional[str] = None
    minimum_threshold: Optional[float] = None

class EvergreenretainerBaseUpdate(BaseModel):
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    etag: Optional[str] = None
    minimum_threshold: Optional[float] = None

class EvergreenretainerBaseDb(BaseModel):
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    etag: Optional[str] = None
    minimum_threshold: Optional[float] = None

