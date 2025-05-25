from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DamagebaseIn(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None
    damage_type: Optional[str] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class DamagebaseOut(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None
    damage_type: Optional[str] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class DamagebaseUpdate(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None
    damage_type: Optional[str] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class DamagebaseDb(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None
    damage_type: Optional[str] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

