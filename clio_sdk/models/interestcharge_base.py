from typing import Optional

from pydantic import BaseModel


class InterestchargeBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None
    total: Optional[float] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class InterestchargeBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None
    total: Optional[float] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class InterestchargeBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None
    total: Optional[float] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class InterestchargeBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None
    total: Optional[float] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

