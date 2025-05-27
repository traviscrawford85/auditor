from typing import Optional

from pydantic import BaseModel


class MatterstageIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    practice_area_id: Optional[str] = None
    name: Optional[str] = None
    order: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MatterstageOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    practice_area_id: Optional[str] = None
    name: Optional[str] = None
    order: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MatterstageUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    practice_area_id: Optional[str] = None
    name: Optional[str] = None
    order: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MatterstageDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    practice_area_id: Optional[str] = None
    name: Optional[str] = None
    order: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

