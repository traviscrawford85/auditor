from typing import Optional

from pydantic import BaseModel


class ParticipantBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    type: Optional[str] = None
    identifier: Optional[str] = None
    secondary_identifier: Optional[str] = None
    enabled: Optional[str] = None
    name: Optional[str] = None
    initials: Optional[str] = None
    job_title_name: Optional[str] = None

class ParticipantBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    type: Optional[str] = None
    identifier: Optional[str] = None
    secondary_identifier: Optional[str] = None
    enabled: Optional[str] = None
    name: Optional[str] = None
    initials: Optional[str] = None
    job_title_name: Optional[str] = None

class ParticipantBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    type: Optional[str] = None
    identifier: Optional[str] = None
    secondary_identifier: Optional[str] = None
    enabled: Optional[str] = None
    name: Optional[str] = None
    initials: Optional[str] = None
    job_title_name: Optional[str] = None

class ParticipantBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    type: Optional[str] = None
    identifier: Optional[str] = None
    secondary_identifier: Optional[str] = None
    enabled: Optional[str] = None
    name: Optional[str] = None
    initials: Optional[str] = None
    job_title_name: Optional[str] = None

