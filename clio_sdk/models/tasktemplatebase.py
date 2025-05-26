from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TasktemplateBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    private: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class TasktemplateBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    private: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class TasktemplateBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    private: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class TasktemplateBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    private: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

