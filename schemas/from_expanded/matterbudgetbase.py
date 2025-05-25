from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MatterbudgetBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    budget: Optional[float] = None
    include_expenses: Optional[bool] = None
    notification_threshold: Optional[int] = None
    notify_users: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class MatterbudgetBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    budget: Optional[float] = None
    include_expenses: Optional[bool] = None
    notification_threshold: Optional[int] = None
    notify_users: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class MatterbudgetBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    budget: Optional[float] = None
    include_expenses: Optional[bool] = None
    notification_threshold: Optional[int] = None
    notify_users: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class MatterbudgetBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    budget: Optional[float] = None
    include_expenses: Optional[bool] = None
    notification_threshold: Optional[int] = None
    notify_users: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

