from typing import Optional

from pydantic import BaseModel


class ActivitycreaterequestdatavendorIn(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatavendorOut(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatavendorUpdate(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatavendorDb(BaseModel):
    id: Optional[str] = None

