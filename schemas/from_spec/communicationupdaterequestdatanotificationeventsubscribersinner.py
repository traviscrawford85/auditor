from typing import Optional

from pydantic import BaseModel


class CommunicationupdaterequestdatanotificationeventsubscribersinnerIn(BaseModel):
    user_id: Optional[str] = None
    id: Optional[str] = None
    _destroy: Optional[str] = None

class CommunicationupdaterequestdatanotificationeventsubscribersinnerOut(BaseModel):
    user_id: Optional[str] = None
    id: Optional[str] = None
    _destroy: Optional[str] = None

class CommunicationupdaterequestdatanotificationeventsubscribersinnerUpdate(BaseModel):
    user_id: Optional[str] = None
    id: Optional[str] = None
    _destroy: Optional[str] = None

class CommunicationupdaterequestdatanotificationeventsubscribersinnerDb(BaseModel):
    user_id: Optional[str] = None
    id: Optional[str] = None
    _destroy: Optional[str] = None

