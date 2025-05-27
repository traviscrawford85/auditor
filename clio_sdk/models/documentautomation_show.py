
from pydantic import BaseModel

from .documentautomation import DocumentautomationOut


class DocumentautomationShowIn(BaseModel):
    data: DocumentautomationIn

class DocumentautomationShowOut(BaseModel):
    data: DocumentautomationOut

class DocumentautomationShowUpdate(BaseModel):
    data: DocumentautomationUpdate

class DocumentautomationShowDb(BaseModel):
    data: DocumentautomationDb

