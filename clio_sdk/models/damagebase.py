from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DamageBaseIn(BaseModel):
    id: Optional[int] = None
    amount: Optional[float] = None
    damage_type: Optional[str] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class DamageBaseOut(BaseModel):
    id: Optional[int] = None
    amount: Optional[float] = None
    damage_type: Optional[str] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class DamageBaseUpdate(BaseModel):
    id: Optional[int] = None
    amount: Optional[float] = None
    damage_type: Optional[str] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class DamageBaseDb(BaseModel):
    id: Optional[int] = None
    amount: Optional[float] = None
    damage_type: Optional[str] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

