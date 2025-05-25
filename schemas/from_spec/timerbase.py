from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TimerbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    start_time: Optional[str] = None
    elapsed_time: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class TimerbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    start_time: Optional[str] = None
    elapsed_time: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class TimerbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    start_time: Optional[str] = None
    elapsed_time: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class TimerbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    start_time: Optional[str] = None
    elapsed_time: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

