from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ParticipantbaseIn(BaseModel):
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

class ParticipantbaseOut(BaseModel):
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

class ParticipantbaseUpdate(BaseModel):
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

class ParticipantbaseDb(BaseModel):
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

