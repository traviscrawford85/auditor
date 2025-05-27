from typing import List

from pydantic import BaseModel

from .documenttemplate import DocumenttemplateOut


class DocumenttemplateListIn(BaseModel):
    data: List[DocumenttemplateIn]

class DocumenttemplateListOut(BaseModel):
    data: List[DocumenttemplateOut]

class DocumenttemplateListUpdate(BaseModel):
    data: List[DocumenttemplateUpdate]

class DocumenttemplateListDb(BaseModel):
    data: List[DocumenttemplateDb]

