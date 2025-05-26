from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumenttemplateListIn(BaseModel):
    data: List[Documenttemplate]

class DocumenttemplateListOut(BaseModel):
    data: List[Documenttemplate]

class DocumenttemplateListUpdate(BaseModel):
    data: List[Documenttemplate]

class DocumenttemplateListDb(BaseModel):
    data: List[Documenttemplate]

