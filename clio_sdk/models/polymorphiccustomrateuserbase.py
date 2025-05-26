from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PolymorphiccustomrateUserBaseIn(BaseModel):
    enabled: Optional[bool] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None

class PolymorphiccustomrateUserBaseOut(BaseModel):
    enabled: Optional[bool] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None

class PolymorphiccustomrateUserBaseUpdate(BaseModel):
    enabled: Optional[bool] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None

class PolymorphiccustomrateUserBaseDb(BaseModel):
    enabled: Optional[bool] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None

