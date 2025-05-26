from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MatterListIn(BaseModel):
    data: List[Matter]

class MatterListOut(BaseModel):
    data: List[Matter]

class MatterListUpdate(BaseModel):
    data: List[Matter]

class MatterListDb(BaseModel):
    data: List[Matter]

