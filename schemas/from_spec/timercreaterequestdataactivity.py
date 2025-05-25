from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TimercreaterequestdataactivityIn(BaseModel):
    id: int

class TimercreaterequestdataactivityOut(BaseModel):
    id: int

class TimercreaterequestdataactivityUpdate(BaseModel):
    id: int

class TimercreaterequestdataactivityDb(BaseModel):
    id: int

