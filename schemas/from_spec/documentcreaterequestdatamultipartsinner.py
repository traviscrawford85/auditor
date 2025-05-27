from typing import Optional

from pydantic import BaseModel


class DocumentcreaterequestdatamultipartsinnerIn(BaseModel):
    part_number: int
    content_length: str
    content_md5: Optional[str] = None

class DocumentcreaterequestdatamultipartsinnerOut(BaseModel):
    part_number: int
    content_length: str
    content_md5: Optional[str] = None

class DocumentcreaterequestdatamultipartsinnerUpdate(BaseModel):
    part_number: int
    content_length: str
    content_md5: Optional[str] = None

class DocumentcreaterequestdatamultipartsinnerDb(BaseModel):
    part_number: int
    content_length: str
    content_md5: Optional[str] = None

