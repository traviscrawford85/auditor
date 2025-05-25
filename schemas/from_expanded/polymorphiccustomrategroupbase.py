from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PolymorphiccustomrateGroupBaseIn(BaseModel):
    etag: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None

class PolymorphiccustomrateGroupBaseOut(BaseModel):
    etag: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None

class PolymorphiccustomrateGroupBaseUpdate(BaseModel):
    etag: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None

class PolymorphiccustomrateGroupBaseDb(BaseModel):
    etag: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None

