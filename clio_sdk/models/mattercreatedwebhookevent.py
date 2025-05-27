from typing import Optional

from pydantic import BaseModel


class MattercreatedwebhookeventIn(BaseModel):
    event: Optional[str] = None
    timestamp: Optional[str] = None
    payload: Optional[dict] = None

class MattercreatedwebhookeventOut(BaseModel):
    event: Optional[str] = None
    timestamp: Optional[str] = None
    payload: Optional[dict] = None

class MattercreatedwebhookeventUpdate(BaseModel):
    event: Optional[str] = None
    timestamp: Optional[str] = None
    payload: Optional[dict] = None

class MattercreatedwebhookeventDb(BaseModel):
    event: Optional[str] = None
    timestamp: Optional[str] = None
    payload: Optional[dict] = None

