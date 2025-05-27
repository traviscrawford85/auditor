from typing import Optional

from pydantic import BaseModel


class MatterbudgetBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    budget: Optional[float] = None
    include_expenses: Optional[bool] = None
    notification_threshold: Optional[int] = None
    notify_users: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MatterbudgetBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    budget: Optional[float] = None
    include_expenses: Optional[bool] = None
    notification_threshold: Optional[int] = None
    notify_users: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MatterbudgetBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    budget: Optional[float] = None
    include_expenses: Optional[bool] = None
    notification_threshold: Optional[int] = None
    notify_users: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MatterbudgetBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    budget: Optional[float] = None
    include_expenses: Optional[bool] = None
    notification_threshold: Optional[int] = None
    notify_users: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

