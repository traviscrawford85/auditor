from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ParticipantBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    type: Optional[str] = None
    identifier: Optional[str] = None
    secondary_identifier: Optional[str] = None
    enabled: Optional[bool] = None
    name: Optional[str] = None
    initials: Optional[str] = None
    job_title_name: Optional[str] = None

class ParticipantBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    type: Optional[str] = None
    identifier: Optional[str] = None
    secondary_identifier: Optional[str] = None
    enabled: Optional[bool] = None
    name: Optional[str] = None
    initials: Optional[str] = None
    job_title_name: Optional[str] = None

class ParticipantBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    type: Optional[str] = None
    identifier: Optional[str] = None
    secondary_identifier: Optional[str] = None
    enabled: Optional[bool] = None
    name: Optional[str] = None
    initials: Optional[str] = None
    job_title_name: Optional[str] = None

class ParticipantBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    type: Optional[str] = None
    identifier: Optional[str] = None
    secondary_identifier: Optional[str] = None
    enabled: Optional[bool] = None
    name: Optional[str] = None
    initials: Optional[str] = None
    job_title_name: Optional[str] = None

