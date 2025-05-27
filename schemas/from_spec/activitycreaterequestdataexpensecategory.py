from typing import Optional

from pydantic import BaseModel


class ActivitycreaterequestdataexpensecategoryIn(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdataexpensecategoryOut(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdataexpensecategoryUpdate(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdataexpensecategoryDb(BaseModel):
    id: Optional[str] = None

