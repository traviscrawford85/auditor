from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class RelatedcontactsListIn(BaseModel):
    data: List[Any]

class RelatedcontactsListOut(BaseModel):
    data: List[Any]

class RelatedcontactsListUpdate(BaseModel):
    data: List[Any]

class RelatedcontactsListDb(BaseModel):
    data: List[Any]

