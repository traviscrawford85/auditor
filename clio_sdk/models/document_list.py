from typing import List

from pydantic import BaseModel

from .document import DocumentOut


class DocumentListIn(BaseModel):
    data: List[DocumentIn]

class DocumentListOut(BaseModel):
    data: List[DocumentOut]

class DocumentListUpdate(BaseModel):
    data: List[DocumentUpdate]

class DocumentListDb(BaseModel):
    data: List[DocumentDb]

