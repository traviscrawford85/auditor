from typing import Optional

from pydantic import BaseModel


class UtbmssetIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class UtbmssetOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class UtbmssetUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class UtbmssetDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

