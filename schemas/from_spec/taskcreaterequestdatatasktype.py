from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TaskcreaterequestdatatasktypeIn(BaseModel):
    id: Optional[str] = None

class TaskcreaterequestdatatasktypeOut(BaseModel):
    id: Optional[str] = None

class TaskcreaterequestdatatasktypeUpdate(BaseModel):
    id: Optional[str] = None

class TaskcreaterequestdatatasktypeDb(BaseModel):
    id: Optional[str] = None

