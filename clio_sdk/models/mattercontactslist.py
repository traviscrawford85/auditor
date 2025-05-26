from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MattercontactsListIn(BaseModel):
    data: List[Mattercontacts]

class MattercontactsListOut(BaseModel):
    data: List[Mattercontacts]

class MattercontactsListUpdate(BaseModel):
    data: List[Mattercontacts]

class MattercontactsListDb(BaseModel):
    data: List[Mattercontacts]

