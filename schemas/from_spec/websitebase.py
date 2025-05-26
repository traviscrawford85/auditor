from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class WebsiteBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    default_web_site: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class WebsiteBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    default_web_site: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class WebsiteBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    default_web_site: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class WebsiteBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    default_web_site: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

