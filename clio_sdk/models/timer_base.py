from typing import Optional

from pydantic import BaseModel


class TimerBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    start_time: Optional[str] = None
    elapsed_time: Optional[float] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class TimerBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    start_time: Optional[str] = None
    elapsed_time: Optional[float] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class TimerBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    start_time: Optional[str] = None
    elapsed_time: Optional[float] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class TimerBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    start_time: Optional[str] = None
    elapsed_time: Optional[float] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

