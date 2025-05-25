from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class SplitinvoicepayerBaseIn(BaseModel):
    id: Optional[int] = None
    contact_id: Optional[int] = None
    matter_id: Optional[int] = None
    send_to_bill_recipients: Optional[bool] = None
    split_portion: Optional[float] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class SplitinvoicepayerBaseOut(BaseModel):
    id: Optional[int] = None
    contact_id: Optional[int] = None
    matter_id: Optional[int] = None
    send_to_bill_recipients: Optional[bool] = None
    split_portion: Optional[float] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class SplitinvoicepayerBaseUpdate(BaseModel):
    id: Optional[int] = None
    contact_id: Optional[int] = None
    matter_id: Optional[int] = None
    send_to_bill_recipients: Optional[bool] = None
    split_portion: Optional[float] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class SplitinvoicepayerBaseDb(BaseModel):
    id: Optional[int] = None
    contact_id: Optional[int] = None
    matter_id: Optional[int] = None
    send_to_bill_recipients: Optional[bool] = None
    split_portion: Optional[float] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

