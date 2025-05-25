from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PolymorphiccustomrateActivitydescriptionBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None

class PolymorphiccustomrateActivitydescriptionBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None

class PolymorphiccustomrateActivitydescriptionBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None

class PolymorphiccustomrateActivitydescriptionBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None

