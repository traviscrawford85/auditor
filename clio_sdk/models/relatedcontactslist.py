from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class RelatedcontactsListIn(BaseModel):
    data: List[Relatedcontacts]

class RelatedcontactsListOut(BaseModel):
    data: List[Relatedcontacts]

class RelatedcontactsListUpdate(BaseModel):
    data: List[Relatedcontacts]

class RelatedcontactsListDb(BaseModel):
    data: List[Relatedcontacts]

