from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class AvatarBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    url: Optional[str] = None
    _destroy: Optional[bool] = None

class AvatarBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    url: Optional[str] = None
    _destroy: Optional[bool] = None

class AvatarBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    url: Optional[str] = None
    _destroy: Optional[bool] = None

class AvatarBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    url: Optional[str] = None
    _destroy: Optional[bool] = None

