from typing import Optional

from pydantic import BaseModel


class ExternalpropertyBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ExternalpropertyBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ExternalpropertyBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ExternalpropertyBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

