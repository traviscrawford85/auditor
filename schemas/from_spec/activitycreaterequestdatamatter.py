from typing import Optional

from pydantic import BaseModel


class ActivitycreaterequestdatamatterIn(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatamatterOut(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatamatterUpdate(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatamatterDb(BaseModel):
    id: Optional[str] = None

