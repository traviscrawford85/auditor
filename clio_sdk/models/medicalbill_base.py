from typing import Optional

from pydantic import BaseModel


class MedicalbillBaseIn(BaseModel):
    id: Optional[int] = None
    adjustment: Optional[float] = None
    amount: Optional[float] = None
    bill_date: Optional[str] = None
    bill_received_date: Optional[str] = None
    damage_type: Optional[str] = None
    document_id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MedicalbillBaseOut(BaseModel):
    id: Optional[int] = None
    adjustment: Optional[float] = None
    amount: Optional[float] = None
    bill_date: Optional[str] = None
    bill_received_date: Optional[str] = None
    damage_type: Optional[str] = None
    document_id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MedicalbillBaseUpdate(BaseModel):
    id: Optional[int] = None
    adjustment: Optional[float] = None
    amount: Optional[float] = None
    bill_date: Optional[str] = None
    bill_received_date: Optional[str] = None
    damage_type: Optional[str] = None
    document_id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MedicalbillBaseDb(BaseModel):
    id: Optional[int] = None
    adjustment: Optional[float] = None
    amount: Optional[float] = None
    bill_date: Optional[str] = None
    bill_received_date: Optional[str] = None
    damage_type: Optional[str] = None
    document_id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

