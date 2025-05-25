from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivitycreaterequestdatataskIn(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatataskOut(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatataskUpdate(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatataskDb(BaseModel):
    id: Optional[str] = None

