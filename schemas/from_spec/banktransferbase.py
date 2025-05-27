from typing import Optional

from pydantic import BaseModel


class BanktransferBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    amount: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None
    primary_authorizer: Optional[str] = None
    secondary_authorizer: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class BanktransferBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    amount: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None
    primary_authorizer: Optional[str] = None
    secondary_authorizer: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class BanktransferBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    amount: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None
    primary_authorizer: Optional[str] = None
    secondary_authorizer: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class BanktransferBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    amount: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None
    primary_authorizer: Optional[str] = None
    secondary_authorizer: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

