from typing import Optional

from pydantic import BaseModel


class BillrecipientBaseIn(BaseModel):
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    on_all_matters: Optional[str] = None
    updated_at: Optional[str] = None

class BillrecipientBaseOut(BaseModel):
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    on_all_matters: Optional[str] = None
    updated_at: Optional[str] = None

class BillrecipientBaseUpdate(BaseModel):
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    on_all_matters: Optional[str] = None
    updated_at: Optional[str] = None

class BillrecipientBaseDb(BaseModel):
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    on_all_matters: Optional[str] = None
    updated_at: Optional[str] = None

