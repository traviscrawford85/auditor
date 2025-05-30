from typing import Optional

from pydantic import BaseModel


class TaskBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    due_at: Optional[str] = None
    permission: Optional[str] = None
    completed_at: Optional[str] = None
    notify_completion: Optional[bool] = None
    statute_of_limitations: Optional[bool] = None
    time_estimated: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    time_entries_count: Optional[int] = None

class TaskBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    due_at: Optional[str] = None
    permission: Optional[str] = None
    completed_at: Optional[str] = None
    notify_completion: Optional[bool] = None
    statute_of_limitations: Optional[bool] = None
    time_estimated: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    time_entries_count: Optional[int] = None

class TaskBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    due_at: Optional[str] = None
    permission: Optional[str] = None
    completed_at: Optional[str] = None
    notify_completion: Optional[bool] = None
    statute_of_limitations: Optional[bool] = None
    time_estimated: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    time_entries_count: Optional[int] = None

class TaskBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    due_at: Optional[str] = None
    permission: Optional[str] = None
    completed_at: Optional[str] = None
    notify_completion: Optional[bool] = None
    statute_of_limitations: Optional[bool] = None
    time_estimated: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    time_entries_count: Optional[int] = None

