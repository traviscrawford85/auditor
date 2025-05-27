from typing import Optional

from pydantic import BaseModel


class TaskcreaterequestdatamatterIn(BaseModel):
    id: Optional[str] = None

class TaskcreaterequestdatamatterOut(BaseModel):
    id: Optional[str] = None

class TaskcreaterequestdatamatterUpdate(BaseModel):
    id: Optional[str] = None

class TaskcreaterequestdatamatterDb(BaseModel):
    id: Optional[str] = None

