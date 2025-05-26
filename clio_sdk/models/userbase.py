from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class UserBaseIn(BaseModel):
    account_owner: Optional[bool] = None
    clio_connect: Optional[bool] = None
    court_rules_default_attendee: Optional[bool] = None
    created_at: Optional[datetime] = None
    default_calendar_id: Optional[int] = None
    email: Optional[str] = None
    enabled: Optional[bool] = None
    etag: Optional[str] = None
    first_name: Optional[str] = None
    id: Optional[int] = None
    initials: Optional[str] = None
    last_name: Optional[str] = None
    name: Optional[str] = None
    phone_number: Optional[str] = None
    rate: Optional[float] = None
    roles: Optional[List[str]] = None
    subscription_type: Optional[str] = None
    time_zone: Optional[str] = None
    updated_at: Optional[datetime] = None

class UserBaseOut(BaseModel):
    account_owner: Optional[bool] = None
    clio_connect: Optional[bool] = None
    court_rules_default_attendee: Optional[bool] = None
    created_at: Optional[datetime] = None
    default_calendar_id: Optional[int] = None
    email: Optional[str] = None
    enabled: Optional[bool] = None
    etag: Optional[str] = None
    first_name: Optional[str] = None
    id: Optional[int] = None
    initials: Optional[str] = None
    last_name: Optional[str] = None
    name: Optional[str] = None
    phone_number: Optional[str] = None
    rate: Optional[float] = None
    roles: Optional[List[str]] = None
    subscription_type: Optional[str] = None
    time_zone: Optional[str] = None
    updated_at: Optional[datetime] = None

class UserBaseUpdate(BaseModel):
    account_owner: Optional[bool] = None
    clio_connect: Optional[bool] = None
    court_rules_default_attendee: Optional[bool] = None
    created_at: Optional[datetime] = None
    default_calendar_id: Optional[int] = None
    email: Optional[str] = None
    enabled: Optional[bool] = None
    etag: Optional[str] = None
    first_name: Optional[str] = None
    id: Optional[int] = None
    initials: Optional[str] = None
    last_name: Optional[str] = None
    name: Optional[str] = None
    phone_number: Optional[str] = None
    rate: Optional[float] = None
    roles: Optional[List[str]] = None
    subscription_type: Optional[str] = None
    time_zone: Optional[str] = None
    updated_at: Optional[datetime] = None

class UserBaseDb(BaseModel):
    account_owner: Optional[bool] = None
    clio_connect: Optional[bool] = None
    court_rules_default_attendee: Optional[bool] = None
    created_at: Optional[datetime] = None
    default_calendar_id: Optional[int] = None
    email: Optional[str] = None
    enabled: Optional[bool] = None
    etag: Optional[str] = None
    first_name: Optional[str] = None
    id: Optional[int] = None
    initials: Optional[str] = None
    last_name: Optional[str] = None
    name: Optional[str] = None
    phone_number: Optional[str] = None
    rate: Optional[float] = None
    roles: Optional[List[str]] = None
    subscription_type: Optional[str] = None
    time_zone: Optional[str] = None
    updated_at: Optional[datetime] = None

