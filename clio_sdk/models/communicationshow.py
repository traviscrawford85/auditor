from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CommunicationShowIn(BaseModel):
    data: Communication

class CommunicationShowOut(BaseModel):
    data: Communication

class CommunicationShowUpdate(BaseModel):
    data: Communication

class CommunicationShowDb(BaseModel):
    data: Communication

