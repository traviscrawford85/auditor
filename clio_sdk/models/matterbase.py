from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MatterBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    number: Optional[int] = None
    display_number: Optional[str] = None
    custom_number: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    location: Optional[str] = None
    client_reference: Optional[str] = None
    client_id: Optional[int] = None
    billable: Optional[bool] = None
    maildrop_address: Optional[str] = None
    billing_method: Optional[str] = None
    open_date: Optional[str] = None
    close_date: Optional[str] = None
    pending_date: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    shared: Optional[bool] = None
    has_tasks: Optional[bool] = None
    last_activity_date: Optional[str] = None
    matter_stage_updated_at: Optional[datetime] = None

class MatterBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    number: Optional[int] = None
    display_number: Optional[str] = None
    custom_number: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    location: Optional[str] = None
    client_reference: Optional[str] = None
    client_id: Optional[int] = None
    billable: Optional[bool] = None
    maildrop_address: Optional[str] = None
    billing_method: Optional[str] = None
    open_date: Optional[str] = None
    close_date: Optional[str] = None
    pending_date: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    shared: Optional[bool] = None
    has_tasks: Optional[bool] = None
    last_activity_date: Optional[str] = None
    matter_stage_updated_at: Optional[datetime] = None

class MatterBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    number: Optional[int] = None
    display_number: Optional[str] = None
    custom_number: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    location: Optional[str] = None
    client_reference: Optional[str] = None
    client_id: Optional[int] = None
    billable: Optional[bool] = None
    maildrop_address: Optional[str] = None
    billing_method: Optional[str] = None
    open_date: Optional[str] = None
    close_date: Optional[str] = None
    pending_date: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    shared: Optional[bool] = None
    has_tasks: Optional[bool] = None
    last_activity_date: Optional[str] = None
    matter_stage_updated_at: Optional[datetime] = None

class MatterBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    number: Optional[int] = None
    display_number: Optional[str] = None
    custom_number: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    location: Optional[str] = None
    client_reference: Optional[str] = None
    client_id: Optional[int] = None
    billable: Optional[bool] = None
    maildrop_address: Optional[str] = None
    billing_method: Optional[str] = None
    open_date: Optional[str] = None
    close_date: Optional[str] = None
    pending_date: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    shared: Optional[bool] = None
    has_tasks: Optional[bool] = None
    last_activity_date: Optional[str] = None
    matter_stage_updated_at: Optional[datetime] = None

