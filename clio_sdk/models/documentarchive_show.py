
from pydantic import BaseModel

from .documentarchive import DocumentarchiveOut


class DocumentarchiveShowIn(BaseModel):
    data: DocumentarchiveIn

class DocumentarchiveShowOut(BaseModel):
    data: DocumentarchiveOut

class DocumentarchiveShowUpdate(BaseModel):
    data: DocumentarchiveUpdate

class DocumentarchiveShowDb(BaseModel):
    data: DocumentarchiveDb

