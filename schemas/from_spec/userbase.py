from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class UserBaseIn(BaseModel):
    account_owner: Optional[str] = None
    clio_connect: Optional[str] = None
    court_rules_default_attendee: Optional[str] = None
    created_at: Optional[str] = None
    default_calendar_id: Optional[str] = None
    email: Optional[str] = None
    enabled: Optional[str] = None
    etag: Optional[str] = None
    first_name: Optional[str] = None
    id: Optional[str] = None
    initials: Optional[str] = None
    last_name: Optional[str] = None
    name: Optional[str] = None
    phone_number: Optional[str] = None
    rate: Optional[str] = None
    roles: Optional[str] = None
    subscription_type: Optional[str] = None
    time_zone: Optional[str] = None
    updated_at: Optional[str] = None

class UserBaseOut(BaseModel):
    account_owner: Optional[str] = None
    clio_connect: Optional[str] = None
    court_rules_default_attendee: Optional[str] = None
    created_at: Optional[str] = None
    default_calendar_id: Optional[str] = None
    email: Optional[str] = None
    enabled: Optional[str] = None
    etag: Optional[str] = None
    first_name: Optional[str] = None
    id: Optional[str] = None
    initials: Optional[str] = None
    last_name: Optional[str] = None
    name: Optional[str] = None
    phone_number: Optional[str] = None
    rate: Optional[str] = None
    roles: Optional[str] = None
    subscription_type: Optional[str] = None
    time_zone: Optional[str] = None
    updated_at: Optional[str] = None

class UserBaseUpdate(BaseModel):
    account_owner: Optional[str] = None
    clio_connect: Optional[str] = None
    court_rules_default_attendee: Optional[str] = None
    created_at: Optional[str] = None
    default_calendar_id: Optional[str] = None
    email: Optional[str] = None
    enabled: Optional[str] = None
    etag: Optional[str] = None
    first_name: Optional[str] = None
    id: Optional[str] = None
    initials: Optional[str] = None
    last_name: Optional[str] = None
    name: Optional[str] = None
    phone_number: Optional[str] = None
    rate: Optional[str] = None
    roles: Optional[str] = None
    subscription_type: Optional[str] = None
    time_zone: Optional[str] = None
    updated_at: Optional[str] = None

class UserBaseDb(BaseModel):
    account_owner: Optional[str] = None
    clio_connect: Optional[str] = None
    court_rules_default_attendee: Optional[str] = None
    created_at: Optional[str] = None
    default_calendar_id: Optional[str] = None
    email: Optional[str] = None
    enabled: Optional[str] = None
    etag: Optional[str] = None
    first_name: Optional[str] = None
    id: Optional[str] = None
    initials: Optional[str] = None
    last_name: Optional[str] = None
    name: Optional[str] = None
    phone_number: Optional[str] = None
    rate: Optional[str] = None
    roles: Optional[str] = None
    subscription_type: Optional[str] = None
    time_zone: Optional[str] = None
    updated_at: Optional[str] = None

