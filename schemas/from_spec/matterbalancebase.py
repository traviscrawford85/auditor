from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MatterbalanceBaseIn(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None

class MatterbalanceBaseOut(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None

class MatterbalanceBaseUpdate(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None

class MatterbalanceBaseDb(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None

