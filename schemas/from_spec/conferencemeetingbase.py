from typing import Optional

from pydantic import BaseModel


class ConferencemeetingBaseIn(BaseModel):
    conference_id: Optional[str] = None
    conference_password: Optional[str] = None
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    join_url: Optional[str] = None
    type: Optional[str] = None
    source_id: Optional[str] = None
    updated_at: Optional[str] = None

class ConferencemeetingBaseOut(BaseModel):
    conference_id: Optional[str] = None
    conference_password: Optional[str] = None
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    join_url: Optional[str] = None
    type: Optional[str] = None
    source_id: Optional[str] = None
    updated_at: Optional[str] = None

class ConferencemeetingBaseUpdate(BaseModel):
    conference_id: Optional[str] = None
    conference_password: Optional[str] = None
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    join_url: Optional[str] = None
    type: Optional[str] = None
    source_id: Optional[str] = None
    updated_at: Optional[str] = None

class ConferencemeetingBaseDb(BaseModel):
    conference_id: Optional[str] = None
    conference_password: Optional[str] = None
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    join_url: Optional[str] = None
    type: Optional[str] = None
    source_id: Optional[str] = None
    updated_at: Optional[str] = None

