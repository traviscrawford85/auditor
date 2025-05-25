from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MattercontactsbaseIn(BaseModel):
    contact_created_at: Optional[str] = None
    contact_updated_at: Optional[str] = None
    created_at: Optional[str] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    first_name: Optional[str] = None
    id: Optional[str] = None
    initials: Optional[str] = None
    is_client: Optional[str] = None
    last_name: Optional[str] = None
    matter_id: Optional[str] = None
    matter_number: Optional[str] = None
    middle_name: Optional[str] = None
    name: Optional[str] = None
    prefix: Optional[str] = None
    primary_email_address: Optional[str] = None
    primary_phone_number: Optional[str] = None
    relationship_name: Optional[str] = None
    secondary_email_address: Optional[str] = None
    secondary_phone_number: Optional[str] = None
    title: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[str] = None
    client_connect_user_id: Optional[str] = None

class MattercontactsbaseOut(BaseModel):
    contact_created_at: Optional[str] = None
    contact_updated_at: Optional[str] = None
    created_at: Optional[str] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    first_name: Optional[str] = None
    id: Optional[str] = None
    initials: Optional[str] = None
    is_client: Optional[str] = None
    last_name: Optional[str] = None
    matter_id: Optional[str] = None
    matter_number: Optional[str] = None
    middle_name: Optional[str] = None
    name: Optional[str] = None
    prefix: Optional[str] = None
    primary_email_address: Optional[str] = None
    primary_phone_number: Optional[str] = None
    relationship_name: Optional[str] = None
    secondary_email_address: Optional[str] = None
    secondary_phone_number: Optional[str] = None
    title: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[str] = None
    client_connect_user_id: Optional[str] = None

class MattercontactsbaseUpdate(BaseModel):
    contact_created_at: Optional[str] = None
    contact_updated_at: Optional[str] = None
    created_at: Optional[str] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    first_name: Optional[str] = None
    id: Optional[str] = None
    initials: Optional[str] = None
    is_client: Optional[str] = None
    last_name: Optional[str] = None
    matter_id: Optional[str] = None
    matter_number: Optional[str] = None
    middle_name: Optional[str] = None
    name: Optional[str] = None
    prefix: Optional[str] = None
    primary_email_address: Optional[str] = None
    primary_phone_number: Optional[str] = None
    relationship_name: Optional[str] = None
    secondary_email_address: Optional[str] = None
    secondary_phone_number: Optional[str] = None
    title: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[str] = None
    client_connect_user_id: Optional[str] = None

class MattercontactsbaseDb(BaseModel):
    contact_created_at: Optional[str] = None
    contact_updated_at: Optional[str] = None
    created_at: Optional[str] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    first_name: Optional[str] = None
    id: Optional[str] = None
    initials: Optional[str] = None
    is_client: Optional[str] = None
    last_name: Optional[str] = None
    matter_id: Optional[str] = None
    matter_number: Optional[str] = None
    middle_name: Optional[str] = None
    name: Optional[str] = None
    prefix: Optional[str] = None
    primary_email_address: Optional[str] = None
    primary_phone_number: Optional[str] = None
    relationship_name: Optional[str] = None
    secondary_email_address: Optional[str] = None
    secondary_phone_number: Optional[str] = None
    title: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[str] = None
    client_connect_user_id: Optional[str] = None

