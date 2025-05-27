from typing import Optional

from pydantic import BaseModel


class BillthemeBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    account_id: Optional[str] = None
    default: Optional[str] = None
    name: Optional[str] = None
    config: Optional[str] = None

class BillthemeBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    account_id: Optional[str] = None
    default: Optional[str] = None
    name: Optional[str] = None
    config: Optional[str] = None

class BillthemeBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    account_id: Optional[str] = None
    default: Optional[str] = None
    name: Optional[str] = None
    config: Optional[str] = None

class BillthemeBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    account_id: Optional[str] = None
    default: Optional[str] = None
    name: Optional[str] = None
    config: Optional[str] = None

