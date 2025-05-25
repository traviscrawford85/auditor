from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LaukcivilcontrolledrateBaseIn(BaseModel):
    id: Optional[int] = None
    activity: Optional[str] = None
    activity_type: Optional[str] = None
    category_of_law: Optional[str] = None
    created_at: Optional[datetime] = None
    etag: Optional[str] = None
    exceptional: Optional[float] = None
    fee: Optional[float] = None
    fee_scheme: Optional[str] = None
    key: Optional[str] = None
    rate_type: Optional[str] = None
    region: Optional[str] = None
    updated_at: Optional[datetime] = None

class LaukcivilcontrolledrateBaseOut(BaseModel):
    id: Optional[int] = None
    activity: Optional[str] = None
    activity_type: Optional[str] = None
    category_of_law: Optional[str] = None
    created_at: Optional[datetime] = None
    etag: Optional[str] = None
    exceptional: Optional[float] = None
    fee: Optional[float] = None
    fee_scheme: Optional[str] = None
    key: Optional[str] = None
    rate_type: Optional[str] = None
    region: Optional[str] = None
    updated_at: Optional[datetime] = None

class LaukcivilcontrolledrateBaseUpdate(BaseModel):
    id: Optional[int] = None
    activity: Optional[str] = None
    activity_type: Optional[str] = None
    category_of_law: Optional[str] = None
    created_at: Optional[datetime] = None
    etag: Optional[str] = None
    exceptional: Optional[float] = None
    fee: Optional[float] = None
    fee_scheme: Optional[str] = None
    key: Optional[str] = None
    rate_type: Optional[str] = None
    region: Optional[str] = None
    updated_at: Optional[datetime] = None

class LaukcivilcontrolledrateBaseDb(BaseModel):
    id: Optional[int] = None
    activity: Optional[str] = None
    activity_type: Optional[str] = None
    category_of_law: Optional[str] = None
    created_at: Optional[datetime] = None
    etag: Optional[str] = None
    exceptional: Optional[float] = None
    fee: Optional[float] = None
    fee_scheme: Optional[str] = None
    key: Optional[str] = None
    rate_type: Optional[str] = None
    region: Optional[str] = None
    updated_at: Optional[datetime] = None

