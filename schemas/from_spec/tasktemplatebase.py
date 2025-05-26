from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TasktemplateBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    private: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class TasktemplateBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    private: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class TasktemplateBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    private: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class TasktemplateBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    private: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

