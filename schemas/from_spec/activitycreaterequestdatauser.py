from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivitycreaterequestdatauserIn(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatauserOut(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatauserUpdate(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatauserDb(BaseModel):
    id: Optional[str] = None

