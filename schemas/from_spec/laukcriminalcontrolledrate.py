from typing import Optional

from pydantic import BaseModel


class LaukcriminalcontrolledrateIn(BaseModel):
    id: Optional[str] = None
    activity: Optional[str] = None
    activity_type: Optional[str] = None
    category_of_law: Optional[str] = None
    counsel: Optional[str] = None
    court: Optional[str] = None
    created_at: Optional[str] = None
    etag: Optional[str] = None
    exceptional: Optional[str] = None
    fee: Optional[str] = None
    fee_scheme: Optional[str] = None
    post_nov_24_exceptional: Optional[str] = None
    post_nov_24_fee: Optional[str] = None
    post_sept_22_exceptional: Optional[str] = None
    post_sept_22_fee: Optional[str] = None
    key: Optional[str] = None
    rate_type: Optional[str] = None
    region: Optional[str] = None
    solicitor_type: Optional[str] = None
    updated_at: Optional[str] = None

class LaukcriminalcontrolledrateOut(BaseModel):
    id: Optional[str] = None
    activity: Optional[str] = None
    activity_type: Optional[str] = None
    category_of_law: Optional[str] = None
    counsel: Optional[str] = None
    court: Optional[str] = None
    created_at: Optional[str] = None
    etag: Optional[str] = None
    exceptional: Optional[str] = None
    fee: Optional[str] = None
    fee_scheme: Optional[str] = None
    post_nov_24_exceptional: Optional[str] = None
    post_nov_24_fee: Optional[str] = None
    post_sept_22_exceptional: Optional[str] = None
    post_sept_22_fee: Optional[str] = None
    key: Optional[str] = None
    rate_type: Optional[str] = None
    region: Optional[str] = None
    solicitor_type: Optional[str] = None
    updated_at: Optional[str] = None

class LaukcriminalcontrolledrateUpdate(BaseModel):
    id: Optional[str] = None
    activity: Optional[str] = None
    activity_type: Optional[str] = None
    category_of_law: Optional[str] = None
    counsel: Optional[str] = None
    court: Optional[str] = None
    created_at: Optional[str] = None
    etag: Optional[str] = None
    exceptional: Optional[str] = None
    fee: Optional[str] = None
    fee_scheme: Optional[str] = None
    post_nov_24_exceptional: Optional[str] = None
    post_nov_24_fee: Optional[str] = None
    post_sept_22_exceptional: Optional[str] = None
    post_sept_22_fee: Optional[str] = None
    key: Optional[str] = None
    rate_type: Optional[str] = None
    region: Optional[str] = None
    solicitor_type: Optional[str] = None
    updated_at: Optional[str] = None

class LaukcriminalcontrolledrateDb(BaseModel):
    id: Optional[str] = None
    activity: Optional[str] = None
    activity_type: Optional[str] = None
    category_of_law: Optional[str] = None
    counsel: Optional[str] = None
    court: Optional[str] = None
    created_at: Optional[str] = None
    etag: Optional[str] = None
    exceptional: Optional[str] = None
    fee: Optional[str] = None
    fee_scheme: Optional[str] = None
    post_nov_24_exceptional: Optional[str] = None
    post_nov_24_fee: Optional[str] = None
    post_sept_22_exceptional: Optional[str] = None
    post_sept_22_fee: Optional[str] = None
    key: Optional[str] = None
    rate_type: Optional[str] = None
    region: Optional[str] = None
    solicitor_type: Optional[str] = None
    updated_at: Optional[str] = None

