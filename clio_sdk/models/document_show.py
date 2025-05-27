
from pydantic import BaseModel

from .document import DocumentOut


class DocumentShowIn(BaseModel):
    data: DocumentIn

class DocumentShowOut(BaseModel):
    data: DocumentOut

class DocumentShowUpdate(BaseModel):
    data: DocumentUpdate

class DocumentShowDb(BaseModel):
    data: DocumentDb

