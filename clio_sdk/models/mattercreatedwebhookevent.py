from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MattercreatedwebhookeventIn(BaseModel):
    event: Optional[str] = None
    timestamp: Optional[datetime] = None
    payload: Optional[Any] = None

class MattercreatedwebhookeventOut(BaseModel):
    event: Optional[str] = None
    timestamp: Optional[datetime] = None
    payload: Optional[Any] = None

class MattercreatedwebhookeventUpdate(BaseModel):
    event: Optional[str] = None
    timestamp: Optional[datetime] = None
    payload: Optional[Any] = None

class MattercreatedwebhookeventDb(BaseModel):
    event: Optional[str] = None
    timestamp: Optional[datetime] = None
    payload: Optional[Any] = None

