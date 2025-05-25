from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class WebsitebaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    default_web_site: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class WebsitebaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    default_web_site: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class WebsitebaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    default_web_site: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class WebsitebaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    default_web_site: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

