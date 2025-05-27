from typing import Optional

from pydantic import BaseModel


class TaskcreaterequestdatatasktypeIn(BaseModel):
    id: Optional[str] = None

class TaskcreaterequestdatatasktypeOut(BaseModel):
    id: Optional[str] = None

class TaskcreaterequestdatatasktypeUpdate(BaseModel):
    id: Optional[str] = None

class TaskcreaterequestdatatasktypeDb(BaseModel):
    id: Optional[str] = None

