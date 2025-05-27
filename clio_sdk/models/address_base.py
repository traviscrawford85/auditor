from typing import Optional

from pydantic import BaseModel


class AddressBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    primary: Optional[bool] = None

class AddressBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    primary: Optional[bool] = None

class AddressBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    primary: Optional[bool] = None

class AddressBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    primary: Optional[bool] = None

