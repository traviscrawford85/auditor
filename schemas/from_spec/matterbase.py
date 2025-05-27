from typing import Optional

from pydantic import BaseModel


class MatterBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    number: Optional[str] = None
    display_number: Optional[str] = None
    custom_number: Optional[str] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    location: Optional[str] = None
    client_reference: Optional[str] = None
    client_id: Optional[str] = None
    billable: Optional[str] = None
    maildrop_address: Optional[str] = None
    billing_method: Optional[str] = None
    open_date: Optional[str] = None
    close_date: Optional[str] = None
    pending_date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    shared: Optional[str] = None
    has_tasks: Optional[str] = None
    last_activity_date: Optional[str] = None
    matter_stage_updated_at: Optional[str] = None

class MatterBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    number: Optional[str] = None
    display_number: Optional[str] = None
    custom_number: Optional[str] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    location: Optional[str] = None
    client_reference: Optional[str] = None
    client_id: Optional[str] = None
    billable: Optional[str] = None
    maildrop_address: Optional[str] = None
    billing_method: Optional[str] = None
    open_date: Optional[str] = None
    close_date: Optional[str] = None
    pending_date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    shared: Optional[str] = None
    has_tasks: Optional[str] = None
    last_activity_date: Optional[str] = None
    matter_stage_updated_at: Optional[str] = None

class MatterBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    number: Optional[str] = None
    display_number: Optional[str] = None
    custom_number: Optional[str] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    location: Optional[str] = None
    client_reference: Optional[str] = None
    client_id: Optional[str] = None
    billable: Optional[str] = None
    maildrop_address: Optional[str] = None
    billing_method: Optional[str] = None
    open_date: Optional[str] = None
    close_date: Optional[str] = None
    pending_date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    shared: Optional[str] = None
    has_tasks: Optional[str] = None
    last_activity_date: Optional[str] = None
    matter_stage_updated_at: Optional[str] = None

class MatterBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    number: Optional[str] = None
    display_number: Optional[str] = None
    custom_number: Optional[str] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    location: Optional[str] = None
    client_reference: Optional[str] = None
    client_id: Optional[str] = None
    billable: Optional[str] = None
    maildrop_address: Optional[str] = None
    billing_method: Optional[str] = None
    open_date: Optional[str] = None
    close_date: Optional[str] = None
    pending_date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    shared: Optional[str] = None
    has_tasks: Optional[str] = None
    last_activity_date: Optional[str] = None
    matter_stage_updated_at: Optional[str] = None

