from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CommunicationemlfilebaseIn(BaseModel):
    id: Optional[str] = None

class CommunicationemlfilebaseOut(BaseModel):
    id: Optional[str] = None

class CommunicationemlfilebaseUpdate(BaseModel):
    id: Optional[str] = None

class CommunicationemlfilebaseDb(BaseModel):
    id: Optional[str] = None

