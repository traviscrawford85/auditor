from typing import Optional

from pydantic import BaseModel


class LaukcivilcertificatedrateBaseIn(BaseModel):
    id: Optional[str] = None
    activity: Optional[str] = None
    activity_sub_category: Optional[str] = None
    activity_type: Optional[str] = None
    attended_several_hearings_for_multiple_clients: Optional[str] = None
    category_of_law: Optional[str] = None
    created_at: Optional[str] = None
    change_of_solicitor: Optional[str] = None
    court: Optional[str] = None
    eligible_for_sqm: Optional[str] = None
    exceptional: Optional[str] = None
    exceptional_warning: Optional[str] = None
    etag: Optional[str] = None
    fee: Optional[str] = None
    fee_scheme: Optional[str] = None
    first_conducting_solicitor: Optional[str] = None
    key: Optional[str] = None
    number_of_clients: Optional[str] = None
    party: Optional[str] = None
    post_transfer_clients_represented: Optional[str] = None
    rate_type: Optional[str] = None
    region: Optional[str] = None
    session_type: Optional[str] = None
    user_type: Optional[str] = None
    updated_at: Optional[str] = None

class LaukcivilcertificatedrateBaseOut(BaseModel):
    id: Optional[str] = None
    activity: Optional[str] = None
    activity_sub_category: Optional[str] = None
    activity_type: Optional[str] = None
    attended_several_hearings_for_multiple_clients: Optional[str] = None
    category_of_law: Optional[str] = None
    created_at: Optional[str] = None
    change_of_solicitor: Optional[str] = None
    court: Optional[str] = None
    eligible_for_sqm: Optional[str] = None
    exceptional: Optional[str] = None
    exceptional_warning: Optional[str] = None
    etag: Optional[str] = None
    fee: Optional[str] = None
    fee_scheme: Optional[str] = None
    first_conducting_solicitor: Optional[str] = None
    key: Optional[str] = None
    number_of_clients: Optional[str] = None
    party: Optional[str] = None
    post_transfer_clients_represented: Optional[str] = None
    rate_type: Optional[str] = None
    region: Optional[str] = None
    session_type: Optional[str] = None
    user_type: Optional[str] = None
    updated_at: Optional[str] = None

class LaukcivilcertificatedrateBaseUpdate(BaseModel):
    id: Optional[str] = None
    activity: Optional[str] = None
    activity_sub_category: Optional[str] = None
    activity_type: Optional[str] = None
    attended_several_hearings_for_multiple_clients: Optional[str] = None
    category_of_law: Optional[str] = None
    created_at: Optional[str] = None
    change_of_solicitor: Optional[str] = None
    court: Optional[str] = None
    eligible_for_sqm: Optional[str] = None
    exceptional: Optional[str] = None
    exceptional_warning: Optional[str] = None
    etag: Optional[str] = None
    fee: Optional[str] = None
    fee_scheme: Optional[str] = None
    first_conducting_solicitor: Optional[str] = None
    key: Optional[str] = None
    number_of_clients: Optional[str] = None
    party: Optional[str] = None
    post_transfer_clients_represented: Optional[str] = None
    rate_type: Optional[str] = None
    region: Optional[str] = None
    session_type: Optional[str] = None
    user_type: Optional[str] = None
    updated_at: Optional[str] = None

class LaukcivilcertificatedrateBaseDb(BaseModel):
    id: Optional[str] = None
    activity: Optional[str] = None
    activity_sub_category: Optional[str] = None
    activity_type: Optional[str] = None
    attended_several_hearings_for_multiple_clients: Optional[str] = None
    category_of_law: Optional[str] = None
    created_at: Optional[str] = None
    change_of_solicitor: Optional[str] = None
    court: Optional[str] = None
    eligible_for_sqm: Optional[str] = None
    exceptional: Optional[str] = None
    exceptional_warning: Optional[str] = None
    etag: Optional[str] = None
    fee: Optional[str] = None
    fee_scheme: Optional[str] = None
    first_conducting_solicitor: Optional[str] = None
    key: Optional[str] = None
    number_of_clients: Optional[str] = None
    party: Optional[str] = None
    post_transfer_clients_represented: Optional[str] = None
    rate_type: Optional[str] = None
    region: Optional[str] = None
    session_type: Optional[str] = None
    user_type: Optional[str] = None
    updated_at: Optional[str] = None

