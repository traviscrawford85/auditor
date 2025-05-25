from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillrecipientbaseIn(BaseModel):
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    on_all_matters: Optional[str] = None
    updated_at: Optional[str] = None

class BillrecipientbaseOut(BaseModel):
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    on_all_matters: Optional[str] = None
    updated_at: Optional[str] = None

class BillrecipientbaseUpdate(BaseModel):
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    on_all_matters: Optional[str] = None
    updated_at: Optional[str] = None

class BillrecipientbaseDb(BaseModel):
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    on_all_matters: Optional[str] = None
    updated_at: Optional[str] = None

