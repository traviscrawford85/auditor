from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivitycreaterequestdatamatterIn(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatamatterOut(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatamatterUpdate(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatamatterDb(BaseModel):
    id: Optional[str] = None

