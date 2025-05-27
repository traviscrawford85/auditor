from typing import Optional

from pydantic import BaseModel


class ActivityrateBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    rate: Optional[float] = None
    flat_rate: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    contact_id: Optional[int] = None
    co_counsel_contact_id: Optional[int] = None

class ActivityrateBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    rate: Optional[float] = None
    flat_rate: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    contact_id: Optional[int] = None
    co_counsel_contact_id: Optional[int] = None

class ActivityrateBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    rate: Optional[float] = None
    flat_rate: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    contact_id: Optional[int] = None
    co_counsel_contact_id: Optional[int] = None

class ActivityrateBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    rate: Optional[float] = None
    flat_rate: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    contact_id: Optional[int] = None
    co_counsel_contact_id: Optional[int] = None

