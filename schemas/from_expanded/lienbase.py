from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LienBaseIn(BaseModel):
    id: Optional[int] = None
    amount: Optional[float] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    lien_type: Optional[str] = None
    mark_as_lien: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class LienBaseOut(BaseModel):
    id: Optional[int] = None
    amount: Optional[float] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    lien_type: Optional[str] = None
    mark_as_lien: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class LienBaseUpdate(BaseModel):
    id: Optional[int] = None
    amount: Optional[float] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    lien_type: Optional[str] = None
    mark_as_lien: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class LienBaseDb(BaseModel):
    id: Optional[int] = None
    amount: Optional[float] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    lien_type: Optional[str] = None
    mark_as_lien: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

