from typing import Optional

from pydantic import BaseModel


class AttendeeBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[bool] = None
    email: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class AttendeeBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[bool] = None
    email: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class AttendeeBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[bool] = None
    email: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class AttendeeBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[bool] = None
    email: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

