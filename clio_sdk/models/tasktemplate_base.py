from typing import Optional

from pydantic import BaseModel


class TasktemplateBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    private: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class TasktemplateBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    private: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class TasktemplateBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    private: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class TasktemplateBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    private: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

