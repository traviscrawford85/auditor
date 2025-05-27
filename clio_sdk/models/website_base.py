from typing import Optional

from pydantic import BaseModel


class WebsiteBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    default_web_site: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class WebsiteBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    default_web_site: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class WebsiteBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    default_web_site: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class WebsiteBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    default_web_site: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

