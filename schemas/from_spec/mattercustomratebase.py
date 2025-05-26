from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MattercustomrateBaseIn(BaseModel):
    type: Optional[str] = None
    on_invoice: Optional[str] = None

class MattercustomrateBaseOut(BaseModel):
    type: Optional[str] = None
    on_invoice: Optional[str] = None

class MattercustomrateBaseUpdate(BaseModel):
    type: Optional[str] = None
    on_invoice: Optional[str] = None

class MattercustomrateBaseDb(BaseModel):
    type: Optional[str] = None
    on_invoice: Optional[str] = None

