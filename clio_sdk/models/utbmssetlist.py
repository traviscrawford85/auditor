from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class UtbmssetListIn(BaseModel):
    data: List[Utbmsset]

class UtbmssetListOut(BaseModel):
    data: List[Utbmsset]

class UtbmssetListUpdate(BaseModel):
    data: List[Utbmsset]

class UtbmssetListDb(BaseModel):
    data: List[Utbmsset]

