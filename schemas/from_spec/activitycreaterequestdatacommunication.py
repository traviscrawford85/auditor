from typing import Optional

from pydantic import BaseModel


class ActivitycreaterequestdatacommunicationIn(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatacommunicationOut(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatacommunicationUpdate(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatacommunicationDb(BaseModel):
    id: Optional[str] = None

