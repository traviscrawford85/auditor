from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CommunicationcreaterequestdatamatterIn(BaseModel):
    id: Optional[str] = None

class CommunicationcreaterequestdatamatterOut(BaseModel):
    id: Optional[str] = None

class CommunicationcreaterequestdatamatterUpdate(BaseModel):
    id: Optional[str] = None

class CommunicationcreaterequestdatamatterDb(BaseModel):
    id: Optional[str] = None

