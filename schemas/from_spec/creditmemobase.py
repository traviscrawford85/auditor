from typing import Optional

from pydantic import BaseModel


class CreditmemoBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[str] = None
    description: Optional[str] = None
    discount: Optional[str] = None
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CreditmemoBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[str] = None
    description: Optional[str] = None
    discount: Optional[str] = None
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CreditmemoBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[str] = None
    description: Optional[str] = None
    discount: Optional[str] = None
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CreditmemoBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[str] = None
    description: Optional[str] = None
    discount: Optional[str] = None
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

