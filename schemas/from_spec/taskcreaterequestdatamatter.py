from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TaskcreaterequestdatamatterIn(BaseModel):
    id: Optional[str] = None

class TaskcreaterequestdatamatterOut(BaseModel):
    id: Optional[str] = None

class TaskcreaterequestdatamatterUpdate(BaseModel):
    id: Optional[str] = None

class TaskcreaterequestdatamatterDb(BaseModel):
    id: Optional[str] = None

