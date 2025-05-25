from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MatterstageBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    practice_area_id: Optional[str] = None
    name: Optional[str] = None
    order: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class MatterstageBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    practice_area_id: Optional[str] = None
    name: Optional[str] = None
    order: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class MatterstageBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    practice_area_id: Optional[str] = None
    name: Optional[str] = None
    order: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class MatterstageBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    practice_area_id: Optional[str] = None
    name: Optional[str] = None
    order: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

