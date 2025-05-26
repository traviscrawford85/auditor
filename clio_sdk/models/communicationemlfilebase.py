from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CommunicationemlfileBaseIn(BaseModel):
    id: Optional[int] = None

class CommunicationemlfileBaseOut(BaseModel):
    id: Optional[int] = None

class CommunicationemlfileBaseUpdate(BaseModel):
    id: Optional[int] = None

class CommunicationemlfileBaseDb(BaseModel):
    id: Optional[int] = None

