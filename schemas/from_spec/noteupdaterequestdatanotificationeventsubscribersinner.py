from typing import Optional

from pydantic import BaseModel


class NoteupdaterequestdatanotificationeventsubscribersinnerIn(BaseModel):
    user_id: Optional[str] = None
    id: Optional[str] = None
    _destroy: Optional[str] = None

class NoteupdaterequestdatanotificationeventsubscribersinnerOut(BaseModel):
    user_id: Optional[str] = None
    id: Optional[str] = None
    _destroy: Optional[str] = None

class NoteupdaterequestdatanotificationeventsubscribersinnerUpdate(BaseModel):
    user_id: Optional[str] = None
    id: Optional[str] = None
    _destroy: Optional[str] = None

class NoteupdaterequestdatanotificationeventsubscribersinnerDb(BaseModel):
    user_id: Optional[str] = None
    id: Optional[str] = None
    _destroy: Optional[str] = None

