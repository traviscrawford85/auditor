from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class AddressIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    primary: Optional[str] = None

class AddressOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    primary: Optional[str] = None

class AddressUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    primary: Optional[str] = None

class AddressDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    primary: Optional[str] = None

