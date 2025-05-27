from typing import Optional

from pydantic import BaseModel


class ActivitycreaterequestdatataskIn(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatataskOut(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatataskUpdate(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatataskDb(BaseModel):
    id: Optional[str] = None

