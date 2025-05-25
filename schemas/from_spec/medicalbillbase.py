from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MedicalbillbaseIn(BaseModel):
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

class MedicalbillbaseOut(BaseModel):
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

class MedicalbillbaseUpdate(BaseModel):
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

class MedicalbillbaseDb(BaseModel):
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

