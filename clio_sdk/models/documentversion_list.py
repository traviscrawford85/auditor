from typing import List

from pydantic import BaseModel

from .documentversion import DocumentversionOut


class DocumentversionListIn(BaseModel):
    data: List[DocumentversionIn]

class DocumentversionListOut(BaseModel):
    data: List[DocumentversionOut]

class DocumentversionListUpdate(BaseModel):
    data: List[DocumentversionUpdate]

class DocumentversionListDb(BaseModel):
    data: List[DocumentversionDb]

