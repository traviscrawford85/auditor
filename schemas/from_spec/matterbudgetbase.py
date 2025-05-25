from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MatterbudgetbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    budget: Optional[str] = None
    include_expenses: Optional[str] = None
    notification_threshold: Optional[str] = None
    notify_users: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MatterbudgetbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    budget: Optional[str] = None
    include_expenses: Optional[str] = None
    notification_threshold: Optional[str] = None
    notify_users: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MatterbudgetbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    budget: Optional[str] = None
    include_expenses: Optional[str] = None
    notification_threshold: Optional[str] = None
    notify_users: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MatterbudgetbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    budget: Optional[str] = None
    include_expenses: Optional[str] = None
    notification_threshold: Optional[str] = None
    notify_users: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

