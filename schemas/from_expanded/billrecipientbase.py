from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillrecipientBaseIn(BaseModel):
    created_at: Optional[datetime] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    on_all_matters: Optional[bool] = None
    updated_at: Optional[datetime] = None

class BillrecipientBaseOut(BaseModel):
    created_at: Optional[datetime] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    on_all_matters: Optional[bool] = None
    updated_at: Optional[datetime] = None

class BillrecipientBaseUpdate(BaseModel):
    created_at: Optional[datetime] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    on_all_matters: Optional[bool] = None
    updated_at: Optional[datetime] = None

class BillrecipientBaseDb(BaseModel):
    created_at: Optional[datetime] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    on_all_matters: Optional[bool] = None
    updated_at: Optional[datetime] = None

