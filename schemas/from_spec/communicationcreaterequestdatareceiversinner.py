from typing import Optional

from pydantic import BaseModel


class CommunicationcreaterequestdatareceiversinnerIn(BaseModel):
    _deleted: Optional[str] = None
    id: Optional[str] = None
    type: Optional[str] = None

class CommunicationcreaterequestdatareceiversinnerOut(BaseModel):
    _deleted: Optional[str] = None
    id: Optional[str] = None
    type: Optional[str] = None

class CommunicationcreaterequestdatareceiversinnerUpdate(BaseModel):
    _deleted: Optional[str] = None
    id: Optional[str] = None
    type: Optional[str] = None

class CommunicationcreaterequestdatareceiversinnerDb(BaseModel):
    _deleted: Optional[str] = None
    id: Optional[str] = None
    type: Optional[str] = None

