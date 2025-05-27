from typing import Optional

from pydantic import BaseModel


class LaukcriminalcontrolledrateBaseIn(BaseModel):
    id: Optional[int] = None
    activity: Optional[str] = None
    activity_type: Optional[str] = None
    category_of_law: Optional[str] = None
    counsel: Optional[str] = None
    court: Optional[str] = None
    created_at: Optional[str] = None
    etag: Optional[str] = None
    exceptional: Optional[float] = None
    fee: Optional[float] = None
    fee_scheme: Optional[str] = None
    post_sept_22_exceptional: Optional[float] = None
    post_sept_22_fee: Optional[float] = None
    key: Optional[str] = None
    rate_type: Optional[str] = None
    region: Optional[str] = None
    solicitor_type: Optional[str] = None
    updated_at: Optional[str] = None

class LaukcriminalcontrolledrateBaseOut(BaseModel):
    id: Optional[int] = None
    activity: Optional[str] = None
    activity_type: Optional[str] = None
    category_of_law: Optional[str] = None
    counsel: Optional[str] = None
    court: Optional[str] = None
    created_at: Optional[str] = None
    etag: Optional[str] = None
    exceptional: Optional[float] = None
    fee: Optional[float] = None
    fee_scheme: Optional[str] = None
    post_sept_22_exceptional: Optional[float] = None
    post_sept_22_fee: Optional[float] = None
    key: Optional[str] = None
    rate_type: Optional[str] = None
    region: Optional[str] = None
    solicitor_type: Optional[str] = None
    updated_at: Optional[str] = None

class LaukcriminalcontrolledrateBaseUpdate(BaseModel):
    id: Optional[int] = None
    activity: Optional[str] = None
    activity_type: Optional[str] = None
    category_of_law: Optional[str] = None
    counsel: Optional[str] = None
    court: Optional[str] = None
    created_at: Optional[str] = None
    etag: Optional[str] = None
    exceptional: Optional[float] = None
    fee: Optional[float] = None
    fee_scheme: Optional[str] = None
    post_sept_22_exceptional: Optional[float] = None
    post_sept_22_fee: Optional[float] = None
    key: Optional[str] = None
    rate_type: Optional[str] = None
    region: Optional[str] = None
    solicitor_type: Optional[str] = None
    updated_at: Optional[str] = None

class LaukcriminalcontrolledrateBaseDb(BaseModel):
    id: Optional[int] = None
    activity: Optional[str] = None
    activity_type: Optional[str] = None
    category_of_law: Optional[str] = None
    counsel: Optional[str] = None
    court: Optional[str] = None
    created_at: Optional[str] = None
    etag: Optional[str] = None
    exceptional: Optional[float] = None
    fee: Optional[float] = None
    fee_scheme: Optional[str] = None
    post_sept_22_exceptional: Optional[float] = None
    post_sept_22_fee: Optional[float] = None
    key: Optional[str] = None
    rate_type: Optional[str] = None
    region: Optional[str] = None
    solicitor_type: Optional[str] = None
    updated_at: Optional[str] = None

