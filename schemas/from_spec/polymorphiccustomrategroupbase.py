from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PolymorphiccustomrategroupBaseIn(BaseModel):
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

class PolymorphiccustomrategroupBaseOut(BaseModel):
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

class PolymorphiccustomrategroupBaseUpdate(BaseModel):
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

class PolymorphiccustomrategroupBaseDb(BaseModel):
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

