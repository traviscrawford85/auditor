from typing import Optional

from pydantic import BaseModel


class CreditmemoBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[float] = None
    description: Optional[str] = None
    discount: Optional[bool] = None
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CreditmemoBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[float] = None
    description: Optional[str] = None
    discount: Optional[bool] = None
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CreditmemoBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[float] = None
    description: Optional[str] = None
    discount: Optional[bool] = None
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CreditmemoBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[float] = None
    description: Optional[str] = None
    discount: Optional[bool] = None
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

