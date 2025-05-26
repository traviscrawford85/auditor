from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LaukexpensecategoryBaseIn(BaseModel):
    certificated: Optional[bool] = None
    civil: Optional[bool] = None
    created_at: Optional[datetime] = None
    criminal: Optional[bool] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    key: Optional[str] = None
    name: Optional[str] = None
    rate: Optional[float] = None
    updated_at: Optional[datetime] = None

class LaukexpensecategoryBaseOut(BaseModel):
    certificated: Optional[bool] = None
    civil: Optional[bool] = None
    created_at: Optional[datetime] = None
    criminal: Optional[bool] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    key: Optional[str] = None
    name: Optional[str] = None
    rate: Optional[float] = None
    updated_at: Optional[datetime] = None

class LaukexpensecategoryBaseUpdate(BaseModel):
    certificated: Optional[bool] = None
    civil: Optional[bool] = None
    created_at: Optional[datetime] = None
    criminal: Optional[bool] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    key: Optional[str] = None
    name: Optional[str] = None
    rate: Optional[float] = None
    updated_at: Optional[datetime] = None

class LaukexpensecategoryBaseDb(BaseModel):
    certificated: Optional[bool] = None
    civil: Optional[bool] = None
    created_at: Optional[datetime] = None
    criminal: Optional[bool] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    key: Optional[str] = None
    name: Optional[str] = None
    rate: Optional[float] = None
    updated_at: Optional[datetime] = None

