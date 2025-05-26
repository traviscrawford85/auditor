from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CommunicationemlfileBaseIn(BaseModel):
    id: Optional[str] = None

class CommunicationemlfileBaseOut(BaseModel):
    id: Optional[str] = None

class CommunicationemlfileBaseUpdate(BaseModel):
    id: Optional[str] = None

class CommunicationemlfileBaseDb(BaseModel):
    id: Optional[str] = None

