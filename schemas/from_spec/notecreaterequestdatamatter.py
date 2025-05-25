from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class NotecreaterequestdatamatterIn(BaseModel):
    id: int

class NotecreaterequestdatamatterOut(BaseModel):
    id: int

class NotecreaterequestdatamatterUpdate(BaseModel):
    id: int

class NotecreaterequestdatamatterDb(BaseModel):
    id: int

