from typing import Optional

from pydantic import BaseModel


class BillthemeIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    account_id: Optional[str] = None
    default: Optional[str] = None
    name: Optional[str] = None
    config: Optional[str] = None

class BillthemeOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    account_id: Optional[str] = None
    default: Optional[str] = None
    name: Optional[str] = None
    config: Optional[str] = None

class BillthemeUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    account_id: Optional[str] = None
    default: Optional[str] = None
    name: Optional[str] = None
    config: Optional[str] = None

class BillthemeDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    account_id: Optional[str] = None
    default: Optional[str] = None
    name: Optional[str] = None
    config: Optional[str] = None

