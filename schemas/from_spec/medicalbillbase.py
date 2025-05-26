from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MedicalbillBaseIn(BaseModel):
    id: Optional[str] = None
    adjustment: Optional[str] = None
    amount: Optional[str] = None
    bill_date: Optional[str] = None
    bill_received_date: Optional[str] = None
    damage_type: Optional[str] = None
    document_id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MedicalbillBaseOut(BaseModel):
    id: Optional[str] = None
    adjustment: Optional[str] = None
    amount: Optional[str] = None
    bill_date: Optional[str] = None
    bill_received_date: Optional[str] = None
    damage_type: Optional[str] = None
    document_id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MedicalbillBaseUpdate(BaseModel):
    id: Optional[str] = None
    adjustment: Optional[str] = None
    amount: Optional[str] = None
    bill_date: Optional[str] = None
    bill_received_date: Optional[str] = None
    damage_type: Optional[str] = None
    document_id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MedicalbillBaseDb(BaseModel):
    id: Optional[str] = None
    adjustment: Optional[str] = None
    amount: Optional[str] = None
    bill_date: Optional[str] = None
    bill_received_date: Optional[str] = None
    damage_type: Optional[str] = None
    document_id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

