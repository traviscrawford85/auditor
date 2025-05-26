from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TasktemplatelistBaseIn(BaseModel):
    created_at: Optional[datetime] = None
    description: Optional[str] = None
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    templates_count: Optional[int] = None
    updated_at: Optional[datetime] = None

class TasktemplatelistBaseOut(BaseModel):
    created_at: Optional[datetime] = None
    description: Optional[str] = None
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    templates_count: Optional[int] = None
    updated_at: Optional[datetime] = None

class TasktemplatelistBaseUpdate(BaseModel):
    created_at: Optional[datetime] = None
    description: Optional[str] = None
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    templates_count: Optional[int] = None
    updated_at: Optional[datetime] = None

class TasktemplatelistBaseDb(BaseModel):
    created_at: Optional[datetime] = None
    description: Optional[str] = None
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    templates_count: Optional[int] = None
    updated_at: Optional[datetime] = None

