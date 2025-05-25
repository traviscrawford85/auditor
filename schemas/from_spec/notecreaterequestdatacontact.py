from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class NotecreaterequestdatacontactIn(BaseModel):
    id: int

class NotecreaterequestdatacontactOut(BaseModel):
    id: int

class NotecreaterequestdatacontactUpdate(BaseModel):
    id: int

class NotecreaterequestdatacontactDb(BaseModel):
    id: int

