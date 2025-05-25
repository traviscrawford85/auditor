from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MattercontactsListIn(BaseModel):
    data: List[Any]

class MattercontactsListOut(BaseModel):
    data: List[Any]

class MattercontactsListUpdate(BaseModel):
    data: List[Any]

class MattercontactsListDb(BaseModel):
    data: List[Any]

