from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MatterbillrecipientBaseIn(BaseModel):
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    updated_at: Optional[str] = None

class MatterbillrecipientBaseOut(BaseModel):
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    updated_at: Optional[str] = None

class MatterbillrecipientBaseUpdate(BaseModel):
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    updated_at: Optional[str] = None

class MatterbillrecipientBaseDb(BaseModel):
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    updated_at: Optional[str] = None

