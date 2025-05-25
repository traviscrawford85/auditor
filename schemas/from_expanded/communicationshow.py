from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CommunicationShowIn(BaseModel):
    data: Any

class CommunicationShowOut(BaseModel):
    data: Any

class CommunicationShowUpdate(BaseModel):
    data: Any

class CommunicationShowDb(BaseModel):
    data: Any

