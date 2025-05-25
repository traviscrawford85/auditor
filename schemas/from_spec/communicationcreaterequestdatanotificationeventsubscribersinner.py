from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CommunicationcreaterequestdatanotificationeventsubscribersinnerIn(BaseModel):
    user_id: str

class CommunicationcreaterequestdatanotificationeventsubscribersinnerOut(BaseModel):
    user_id: str

class CommunicationcreaterequestdatanotificationeventsubscribersinnerUpdate(BaseModel):
    user_id: str

class CommunicationcreaterequestdatanotificationeventsubscribersinnerDb(BaseModel):
    user_id: str

