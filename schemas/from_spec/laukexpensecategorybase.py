from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LaukexpensecategorybaseIn(BaseModel):
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

class LaukexpensecategorybaseOut(BaseModel):
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

class LaukexpensecategorybaseUpdate(BaseModel):
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

class LaukexpensecategorybaseDb(BaseModel):
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

