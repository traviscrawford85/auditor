from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MatterbillrecipientBaseIn(BaseModel):
    created_at: Optional[datetime] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    updated_at: Optional[datetime] = None

class MatterbillrecipientBaseOut(BaseModel):
    created_at: Optional[datetime] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    updated_at: Optional[datetime] = None

class MatterbillrecipientBaseUpdate(BaseModel):
    created_at: Optional[datetime] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    updated_at: Optional[datetime] = None

class MatterbillrecipientBaseDb(BaseModel):
    created_at: Optional[datetime] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    updated_at: Optional[datetime] = None

