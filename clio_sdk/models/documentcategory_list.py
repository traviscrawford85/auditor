from typing import List

from pydantic import BaseModel

from .documentcategory import DocumentcategoryOut


class DocumentcategoryListIn(BaseModel):
    data: List[DocumentcategoryIn]

class DocumentcategoryListOut(BaseModel):
    data: List[DocumentcategoryOut]

class DocumentcategoryListUpdate(BaseModel):
    data: List[DocumentcategoryUpdate]

class DocumentcategoryListDb(BaseModel):
    data: List[DocumentcategoryDb]

