from typing import Optional

from pydantic import BaseModel


class RelatedcontactsBaseIn(BaseModel):
    id: Optional[str] = None
    contact_id: Optional[str] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    type: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    prefix: Optional[str] = None
    title: Optional[str] = None
    initials: Optional[str] = None
    is_matter_client: Optional[str] = None
    primary_email_address: Optional[str] = None
    primary_phone_number: Optional[str] = None
    client_connect_user_id: Optional[str] = None

class RelatedcontactsBaseOut(BaseModel):
    id: Optional[str] = None
    contact_id: Optional[str] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    type: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    prefix: Optional[str] = None
    title: Optional[str] = None
    initials: Optional[str] = None
    is_matter_client: Optional[str] = None
    primary_email_address: Optional[str] = None
    primary_phone_number: Optional[str] = None
    client_connect_user_id: Optional[str] = None

class RelatedcontactsBaseUpdate(BaseModel):
    id: Optional[str] = None
    contact_id: Optional[str] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    type: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    prefix: Optional[str] = None
    title: Optional[str] = None
    initials: Optional[str] = None
    is_matter_client: Optional[str] = None
    primary_email_address: Optional[str] = None
    primary_phone_number: Optional[str] = None
    client_connect_user_id: Optional[str] = None

class RelatedcontactsBaseDb(BaseModel):
    id: Optional[str] = None
    contact_id: Optional[str] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    type: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    prefix: Optional[str] = None
    title: Optional[str] = None
    initials: Optional[str] = None
    is_matter_client: Optional[str] = None
    primary_email_address: Optional[str] = None
    primary_phone_number: Optional[str] = None
    client_connect_user_id: Optional[str] = None

