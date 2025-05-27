
from pydantic import BaseModel

from .documenttemplate import DocumenttemplateOut


class DocumenttemplateShowIn(BaseModel):
    data: DocumenttemplateIn

class DocumenttemplateShowOut(BaseModel):
    data: DocumenttemplateOut

class DocumenttemplateShowUpdate(BaseModel):
    data: DocumenttemplateUpdate

class DocumenttemplateShowDb(BaseModel):
    data: DocumenttemplateDb

