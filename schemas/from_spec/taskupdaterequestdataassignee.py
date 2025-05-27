from typing import Optional

from pydantic import BaseModel


class TaskupdaterequestdataassigneeIn(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None

class TaskupdaterequestdataassigneeOut(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None

class TaskupdaterequestdataassigneeUpdate(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None

class TaskupdaterequestdataassigneeDb(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None

