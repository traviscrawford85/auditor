from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MattercontactsBaseIn(BaseModel):
    contact_created_at: Optional[datetime] = None
    contact_updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    first_name: Optional[str] = None
    id: Optional[int] = None
    initials: Optional[str] = None
    is_client: Optional[bool] = None
    last_name: Optional[str] = None
    matter_id: Optional[int] = None
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
    updated_at: Optional[datetime] = None
    client_connect_user_id: Optional[int] = None

class MattercontactsBaseOut(BaseModel):
    contact_created_at: Optional[datetime] = None
    contact_updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    first_name: Optional[str] = None
    id: Optional[int] = None
    initials: Optional[str] = None
    is_client: Optional[bool] = None
    last_name: Optional[str] = None
    matter_id: Optional[int] = None
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
    updated_at: Optional[datetime] = None
    client_connect_user_id: Optional[int] = None

class MattercontactsBaseUpdate(BaseModel):
    contact_created_at: Optional[datetime] = None
    contact_updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    first_name: Optional[str] = None
    id: Optional[int] = None
    initials: Optional[str] = None
    is_client: Optional[bool] = None
    last_name: Optional[str] = None
    matter_id: Optional[int] = None
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
    updated_at: Optional[datetime] = None
    client_connect_user_id: Optional[int] = None

class MattercontactsBaseDb(BaseModel):
    contact_created_at: Optional[datetime] = None
    contact_updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    first_name: Optional[str] = None
    id: Optional[int] = None
    initials: Optional[str] = None
    is_client: Optional[bool] = None
    last_name: Optional[str] = None
    matter_id: Optional[int] = None
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
    updated_at: Optional[datetime] = None
    client_connect_user_id: Optional[int] = None

