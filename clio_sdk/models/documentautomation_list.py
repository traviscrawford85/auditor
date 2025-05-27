from typing import List

from pydantic import BaseModel

from .documentautomation import DocumentautomationOut


class DocumentautomationListIn(BaseModel):
    data: List[DocumentautomationIn]

class DocumentautomationListOut(BaseModel):
    data: List[DocumentautomationOut]

class DocumentautomationListUpdate(BaseModel):
    data: List[DocumentautomationUpdate]

class DocumentautomationListDb(BaseModel):
    data: List[DocumentautomationDb]

