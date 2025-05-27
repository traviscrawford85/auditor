from typing import Optional

from pydantic import BaseModel


class ActivitycreaterequestdatacontactnoteIn(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatacontactnoteOut(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatacontactnoteUpdate(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatacontactnoteDb(BaseModel):
    id: Optional[str] = None

