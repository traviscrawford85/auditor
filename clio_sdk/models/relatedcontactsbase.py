from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class RelatedcontactsBaseIn(BaseModel):
    id: Optional[int] = None
    contact_id: Optional[int] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    type: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    prefix: Optional[str] = None
    title: Optional[str] = None
    initials: Optional[str] = None
    is_matter_client: Optional[bool] = None
    primary_email_address: Optional[str] = None
    primary_phone_number: Optional[str] = None
    client_connect_user_id: Optional[int] = None

class RelatedcontactsBaseOut(BaseModel):
    id: Optional[int] = None
    contact_id: Optional[int] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    type: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    prefix: Optional[str] = None
    title: Optional[str] = None
    initials: Optional[str] = None
    is_matter_client: Optional[bool] = None
    primary_email_address: Optional[str] = None
    primary_phone_number: Optional[str] = None
    client_connect_user_id: Optional[int] = None

class RelatedcontactsBaseUpdate(BaseModel):
    id: Optional[int] = None
    contact_id: Optional[int] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    type: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    prefix: Optional[str] = None
    title: Optional[str] = None
    initials: Optional[str] = None
    is_matter_client: Optional[bool] = None
    primary_email_address: Optional[str] = None
    primary_phone_number: Optional[str] = None
    client_connect_user_id: Optional[int] = None

class RelatedcontactsBaseDb(BaseModel):
    id: Optional[int] = None
    contact_id: Optional[int] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    type: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    prefix: Optional[str] = None
    title: Optional[str] = None
    initials: Optional[str] = None
    is_matter_client: Optional[bool] = None
    primary_email_address: Optional[str] = None
    primary_phone_number: Optional[str] = None
    client_connect_user_id: Optional[int] = None

