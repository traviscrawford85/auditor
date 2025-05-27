from typing import Optional

from pydantic import BaseModel


class TasktemplatelistBaseIn(BaseModel):
    created_at: Optional[str] = None
    description: Optional[str] = None
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    templates_count: Optional[int] = None
    updated_at: Optional[str] = None

class TasktemplatelistBaseOut(BaseModel):
    created_at: Optional[str] = None
    description: Optional[str] = None
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    templates_count: Optional[int] = None
    updated_at: Optional[str] = None

class TasktemplatelistBaseUpdate(BaseModel):
    created_at: Optional[str] = None
    description: Optional[str] = None
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    templates_count: Optional[int] = None
    updated_at: Optional[str] = None

class TasktemplatelistBaseDb(BaseModel):
    created_at: Optional[str] = None
    description: Optional[str] = None
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    templates_count: Optional[int] = None
    updated_at: Optional[str] = None

