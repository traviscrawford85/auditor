from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MatterdocketcreaterequestdatatriggerIn(BaseModel):
    id: int

class MatterdocketcreaterequestdatatriggerOut(BaseModel):
    id: int

class MatterdocketcreaterequestdatatriggerUpdate(BaseModel):
    id: int

class MatterdocketcreaterequestdatatriggerDb(BaseModel):
    id: int

