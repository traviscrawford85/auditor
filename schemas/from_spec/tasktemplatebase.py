from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TasktemplatebaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    private: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class TasktemplatebaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    private: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class TasktemplatebaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    private: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class TasktemplatebaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    private: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

