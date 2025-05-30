from typing import Optional

from pydantic import BaseModel


class PolymorphiccustomrateBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    rate: Optional[str] = None
    award: Optional[str] = None
    note: Optional[str] = None
    date: Optional[str] = None

class PolymorphiccustomrateBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    rate: Optional[str] = None
    award: Optional[str] = None
    note: Optional[str] = None
    date: Optional[str] = None

class PolymorphiccustomrateBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    rate: Optional[str] = None
    award: Optional[str] = None
    note: Optional[str] = None
    date: Optional[str] = None

class PolymorphiccustomrateBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    rate: Optional[str] = None
    award: Optional[str] = None
    note: Optional[str] = None
    date: Optional[str] = None

