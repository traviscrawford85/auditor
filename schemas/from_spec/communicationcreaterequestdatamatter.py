from typing import Optional

from pydantic import BaseModel


class CommunicationcreaterequestdatamatterIn(BaseModel):
    id: Optional[str] = None

class CommunicationcreaterequestdatamatterOut(BaseModel):
    id: Optional[str] = None

class CommunicationcreaterequestdatamatterUpdate(BaseModel):
    id: Optional[str] = None

class CommunicationcreaterequestdatamatterDb(BaseModel):
    id: Optional[str] = None

