from typing import Optional

from pydantic import BaseModel


class PolymorphiccustomrateBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    rate: Optional[float] = None
    award: Optional[float] = None
    note: Optional[str] = None
    date: Optional[str] = None

class PolymorphiccustomrateBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    rate: Optional[float] = None
    award: Optional[float] = None
    note: Optional[str] = None
    date: Optional[str] = None

class PolymorphiccustomrateBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    rate: Optional[float] = None
    award: Optional[float] = None
    note: Optional[str] = None
    date: Optional[str] = None

class PolymorphiccustomrateBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    rate: Optional[float] = None
    award: Optional[float] = None
    note: Optional[str] = None
    date: Optional[str] = None

