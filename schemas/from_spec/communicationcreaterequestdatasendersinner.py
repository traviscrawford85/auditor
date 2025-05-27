from typing import Optional

from pydantic import BaseModel


class CommunicationcreaterequestdatasendersinnerIn(BaseModel):
    _deleted: Optional[str] = None
    id: Optional[str] = None
    type: Optional[str] = None

class CommunicationcreaterequestdatasendersinnerOut(BaseModel):
    _deleted: Optional[str] = None
    id: Optional[str] = None
    type: Optional[str] = None

class CommunicationcreaterequestdatasendersinnerUpdate(BaseModel):
    _deleted: Optional[str] = None
    id: Optional[str] = None
    type: Optional[str] = None

class CommunicationcreaterequestdatasendersinnerDb(BaseModel):
    _deleted: Optional[str] = None
    id: Optional[str] = None
    type: Optional[str] = None

