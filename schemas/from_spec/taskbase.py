from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TaskbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    due_at: Optional[str] = None
    permission: Optional[str] = None
    completed_at: Optional[str] = None
    notify_completion: Optional[str] = None
    statute_of_limitations: Optional[str] = None
    time_estimated: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    time_entries_count: Optional[str] = None

class TaskbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    due_at: Optional[str] = None
    permission: Optional[str] = None
    completed_at: Optional[str] = None
    notify_completion: Optional[str] = None
    statute_of_limitations: Optional[str] = None
    time_estimated: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    time_entries_count: Optional[str] = None

class TaskbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    due_at: Optional[str] = None
    permission: Optional[str] = None
    completed_at: Optional[str] = None
    notify_completion: Optional[str] = None
    statute_of_limitations: Optional[str] = None
    time_estimated: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    time_entries_count: Optional[str] = None

class TaskbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    due_at: Optional[str] = None
    permission: Optional[str] = None
    completed_at: Optional[str] = None
    notify_completion: Optional[str] = None
    statute_of_limitations: Optional[str] = None
    time_estimated: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    time_entries_count: Optional[str] = None

