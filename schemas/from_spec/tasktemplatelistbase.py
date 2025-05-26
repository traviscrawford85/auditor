from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TasktemplatelistBaseIn(BaseModel):
    created_at: Optional[str] = None
    description: Optional[str] = None
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    templates_count: Optional[str] = None
    updated_at: Optional[str] = None

class TasktemplatelistBaseOut(BaseModel):
    created_at: Optional[str] = None
    description: Optional[str] = None
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    templates_count: Optional[str] = None
    updated_at: Optional[str] = None

class TasktemplatelistBaseUpdate(BaseModel):
    created_at: Optional[str] = None
    description: Optional[str] = None
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    templates_count: Optional[str] = None
    updated_at: Optional[str] = None

class TasktemplatelistBaseDb(BaseModel):
    created_at: Optional[str] = None
    description: Optional[str] = None
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    templates_count: Optional[str] = None
    updated_at: Optional[str] = None

