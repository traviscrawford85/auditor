from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumenttemplateListIn(BaseModel):
    data: List[Any]

class DocumenttemplateListOut(BaseModel):
    data: List[Any]

class DocumenttemplateListUpdate(BaseModel):
    data: List[Any]

class DocumenttemplateListDb(BaseModel):
    data: List[Any]

