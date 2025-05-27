
from pydantic import BaseModel

from .documentcategory import DocumentcategoryOut


class DocumentcategoryShowIn(BaseModel):
    data: DocumentcategoryIn

class DocumentcategoryShowOut(BaseModel):
    data: DocumentcategoryOut

class DocumentcategoryShowUpdate(BaseModel):
    data: DocumentcategoryUpdate

class DocumentcategoryShowDb(BaseModel):
    data: DocumentcategoryDb

