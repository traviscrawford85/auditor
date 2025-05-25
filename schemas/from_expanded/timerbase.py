from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TimerBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    start_time: Optional[datetime] = None
    elapsed_time: Optional[float] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class TimerBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    start_time: Optional[datetime] = None
    elapsed_time: Optional[float] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class TimerBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    start_time: Optional[datetime] = None
    elapsed_time: Optional[float] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class TimerBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    start_time: Optional[datetime] = None
    elapsed_time: Optional[float] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

