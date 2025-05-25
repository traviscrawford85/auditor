from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LaukexpensecategoryIn(BaseModel):
    certificated: Optional[str] = None
    civil: Optional[str] = None
    created_at: Optional[str] = None
    criminal: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    key: Optional[str] = None
    name: Optional[str] = None
    rate: Optional[str] = None
    updated_at: Optional[str] = None

class LaukexpensecategoryOut(BaseModel):
    certificated: Optional[str] = None
    civil: Optional[str] = None
    created_at: Optional[str] = None
    criminal: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    key: Optional[str] = None
    name: Optional[str] = None
    rate: Optional[str] = None
    updated_at: Optional[str] = None

class LaukexpensecategoryUpdate(BaseModel):
    certificated: Optional[str] = None
    civil: Optional[str] = None
    created_at: Optional[str] = None
    criminal: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    key: Optional[str] = None
    name: Optional[str] = None
    rate: Optional[str] = None
    updated_at: Optional[str] = None

class LaukexpensecategoryDb(BaseModel):
    certificated: Optional[str] = None
    civil: Optional[str] = None
    created_at: Optional[str] = None
    criminal: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    key: Optional[str] = None
    name: Optional[str] = None
    rate: Optional[str] = None
    updated_at: Optional[str] = None

