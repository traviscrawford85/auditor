from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PolymorphiccustomrategroupbaseIn(BaseModel):
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

class PolymorphiccustomrategroupbaseOut(BaseModel):
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

class PolymorphiccustomrategroupbaseUpdate(BaseModel):
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

class PolymorphiccustomrategroupbaseDb(BaseModel):
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

