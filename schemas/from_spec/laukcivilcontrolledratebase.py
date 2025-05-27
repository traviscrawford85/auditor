from typing import Optional

from pydantic import BaseModel


class LaukcivilcontrolledrateBaseIn(BaseModel):
    id: Optional[str] = None
    activity: Optional[str] = None
    activity_type: Optional[str] = None
    category_of_law: Optional[str] = None
    created_at: Optional[str] = None
    etag: Optional[str] = None
    exceptional: Optional[str] = None
    fee: Optional[str] = None
    fee_scheme: Optional[str] = None
    key: Optional[str] = None
    rate_type: Optional[str] = None
    region: Optional[str] = None
    updated_at: Optional[str] = None

class LaukcivilcontrolledrateBaseOut(BaseModel):
    id: Optional[str] = None
    activity: Optional[str] = None
    activity_type: Optional[str] = None
    category_of_law: Optional[str] = None
    created_at: Optional[str] = None
    etag: Optional[str] = None
    exceptional: Optional[str] = None
    fee: Optional[str] = None
    fee_scheme: Optional[str] = None
    key: Optional[str] = None
    rate_type: Optional[str] = None
    region: Optional[str] = None
    updated_at: Optional[str] = None

class LaukcivilcontrolledrateBaseUpdate(BaseModel):
    id: Optional[str] = None
    activity: Optional[str] = None
    activity_type: Optional[str] = None
    category_of_law: Optional[str] = None
    created_at: Optional[str] = None
    etag: Optional[str] = None
    exceptional: Optional[str] = None
    fee: Optional[str] = None
    fee_scheme: Optional[str] = None
    key: Optional[str] = None
    rate_type: Optional[str] = None
    region: Optional[str] = None
    updated_at: Optional[str] = None

class LaukcivilcontrolledrateBaseDb(BaseModel):
    id: Optional[str] = None
    activity: Optional[str] = None
    activity_type: Optional[str] = None
    category_of_law: Optional[str] = None
    created_at: Optional[str] = None
    etag: Optional[str] = None
    exceptional: Optional[str] = None
    fee: Optional[str] = None
    fee_scheme: Optional[str] = None
    key: Optional[str] = None
    rate_type: Optional[str] = None
    region: Optional[str] = None
    updated_at: Optional[str] = None

