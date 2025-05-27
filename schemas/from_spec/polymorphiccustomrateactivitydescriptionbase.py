from typing import Optional

from pydantic import BaseModel


class PolymorphiccustomrateactivitydescriptionBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None

class PolymorphiccustomrateactivitydescriptionBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None

class PolymorphiccustomrateactivitydescriptionBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None

class PolymorphiccustomrateactivitydescriptionBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None

