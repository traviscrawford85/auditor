from typing import Optional

from pydantic import BaseModel


class RemindertemplateBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    duration: Optional[int] = None
    notification_type: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class RemindertemplateBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    duration: Optional[int] = None
    notification_type: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class RemindertemplateBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    duration: Optional[int] = None
    notification_type: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class RemindertemplateBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    duration: Optional[int] = None
    notification_type: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

