from typing import Optional

from pydantic import BaseModel


class ActivitycreaterequestdatauserIn(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatauserOut(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatauserUpdate(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatauserDb(BaseModel):
    id: Optional[str] = None

