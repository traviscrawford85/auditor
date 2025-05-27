from typing import Optional

from pydantic import BaseModel


class MatterbudgetBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    budget: Optional[str] = None
    include_expenses: Optional[str] = None
    notification_threshold: Optional[str] = None
    notify_users: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MatterbudgetBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    budget: Optional[str] = None
    include_expenses: Optional[str] = None
    notification_threshold: Optional[str] = None
    notify_users: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MatterbudgetBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    budget: Optional[str] = None
    include_expenses: Optional[str] = None
    notification_threshold: Optional[str] = None
    notify_users: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MatterbudgetBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    budget: Optional[str] = None
    include_expenses: Optional[str] = None
    notification_threshold: Optional[str] = None
    notify_users: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

