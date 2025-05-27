from typing import Optional

from pydantic import BaseModel


class MattercreaterequestdatamatterbudgetIn(BaseModel):
    _destroy: Optional[str] = None
    budget: Optional[str] = None
    include_expenses: Optional[str] = None
    notification_threshold: Optional[str] = None
    notify_users: Optional[str] = None

class MattercreaterequestdatamatterbudgetOut(BaseModel):
    _destroy: Optional[str] = None
    budget: Optional[str] = None
    include_expenses: Optional[str] = None
    notification_threshold: Optional[str] = None
    notify_users: Optional[str] = None

class MattercreaterequestdatamatterbudgetUpdate(BaseModel):
    _destroy: Optional[str] = None
    budget: Optional[str] = None
    include_expenses: Optional[str] = None
    notification_threshold: Optional[str] = None
    notify_users: Optional[str] = None

class MattercreaterequestdatamatterbudgetDb(BaseModel):
    _destroy: Optional[str] = None
    budget: Optional[str] = None
    include_expenses: Optional[str] = None
    notification_threshold: Optional[str] = None
    notify_users: Optional[str] = None

