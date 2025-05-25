from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class GrantbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    funding_code: Optional[str] = None
    funding_code_and_name: Optional[str] = None
    funding_source_name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    balance: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None

class GrantbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    funding_code: Optional[str] = None
    funding_code_and_name: Optional[str] = None
    funding_source_name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    balance: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None

class GrantbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    funding_code: Optional[str] = None
    funding_code_and_name: Optional[str] = None
    funding_source_name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    balance: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None

class GrantbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    funding_code: Optional[str] = None
    funding_code_and_name: Optional[str] = None
    funding_source_name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    balance: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None

