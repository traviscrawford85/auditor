from typing import Optional

from pydantic import BaseModel


class MatterstageBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    practice_area_id: Optional[str] = None
    name: Optional[str] = None
    order: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MatterstageBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    practice_area_id: Optional[str] = None
    name: Optional[str] = None
    order: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MatterstageBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    practice_area_id: Optional[str] = None
    name: Optional[str] = None
    order: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MatterstageBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    practice_area_id: Optional[str] = None
    name: Optional[str] = None
    order: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

