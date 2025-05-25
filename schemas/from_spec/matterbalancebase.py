from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MatterbalancebaseIn(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None

class MatterbalancebaseOut(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None

class MatterbalancebaseUpdate(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None

class MatterbalancebaseDb(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None

