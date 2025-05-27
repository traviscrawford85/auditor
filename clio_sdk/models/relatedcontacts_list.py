from typing import List

from pydantic import BaseModel

from .relatedcontacts import RelatedcontactsOut


class RelatedcontactsListIn(BaseModel):
    data: List[RelatedcontactsIn]

class RelatedcontactsListOut(BaseModel):
    data: List[RelatedcontactsOut]

class RelatedcontactsListUpdate(BaseModel):
    data: List[RelatedcontactsUpdate]

class RelatedcontactsListDb(BaseModel):
    data: List[RelatedcontactsDb]

