from typing import Optional

from pydantic import BaseModel


class GrantBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    funding_code: Optional[str] = None
    funding_code_and_name: Optional[str] = None
    funding_source_name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    balance: Optional[str] = None

class GrantBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    funding_code: Optional[str] = None
    funding_code_and_name: Optional[str] = None
    funding_source_name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    balance: Optional[str] = None

class GrantBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    funding_code: Optional[str] = None
    funding_code_and_name: Optional[str] = None
    funding_source_name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    balance: Optional[str] = None

class GrantBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    funding_code: Optional[str] = None
    funding_code_and_name: Optional[str] = None
    funding_source_name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    balance: Optional[str] = None

