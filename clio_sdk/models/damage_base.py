from typing import Optional

from pydantic import BaseModel


class DamageBaseIn(BaseModel):
    id: Optional[int] = None
    amount: Optional[float] = None
    damage_type: Optional[str] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class DamageBaseOut(BaseModel):
    id: Optional[int] = None
    amount: Optional[float] = None
    damage_type: Optional[str] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class DamageBaseUpdate(BaseModel):
    id: Optional[int] = None
    amount: Optional[float] = None
    damage_type: Optional[str] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class DamageBaseDb(BaseModel):
    id: Optional[int] = None
    amount: Optional[float] = None
    damage_type: Optional[str] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

