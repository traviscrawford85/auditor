from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivitycreaterequestdatacommunicationIn(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatacommunicationOut(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatacommunicationUpdate(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatacommunicationDb(BaseModel):
    id: Optional[str] = None

