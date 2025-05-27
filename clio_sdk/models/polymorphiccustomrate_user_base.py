from typing import Optional

from pydantic import BaseModel


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

