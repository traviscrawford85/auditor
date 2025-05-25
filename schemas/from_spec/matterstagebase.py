from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MatterstagebaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    practice_area_id: Optional[str] = None
    name: Optional[str] = None
    order: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MatterstagebaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    practice_area_id: Optional[str] = None
    name: Optional[str] = None
    order: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MatterstagebaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    practice_area_id: Optional[str] = None
    name: Optional[str] = None
    order: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MatterstagebaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    practice_area_id: Optional[str] = None
    name: Optional[str] = None
    order: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

