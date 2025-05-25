from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MattercustomratebaseIn(BaseModel):
    type: Optional[str] = None
    on_invoice: Optional[str] = None

class MattercustomratebaseOut(BaseModel):
    type: Optional[str] = None
    on_invoice: Optional[str] = None

class MattercustomratebaseUpdate(BaseModel):
    type: Optional[str] = None
    on_invoice: Optional[str] = None

class MattercustomratebaseDb(BaseModel):
    type: Optional[str] = None
    on_invoice: Optional[str] = None

