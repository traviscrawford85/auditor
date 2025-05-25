from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PolymorphiccustomrateuserbaseIn(BaseModel):
    enabled: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

class PolymorphiccustomrateuserbaseOut(BaseModel):
    enabled: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

class PolymorphiccustomrateuserbaseUpdate(BaseModel):
    enabled: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

class PolymorphiccustomrateuserbaseDb(BaseModel):
    enabled: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

