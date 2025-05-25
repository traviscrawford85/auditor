from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentupdaterequestdatamultipartsinnerIn(BaseModel):
    part_number: Optional[str] = None
    content_length: Optional[str] = None
    content_md5: Optional[str] = None

class DocumentupdaterequestdatamultipartsinnerOut(BaseModel):
    part_number: Optional[str] = None
    content_length: Optional[str] = None
    content_md5: Optional[str] = None

class DocumentupdaterequestdatamultipartsinnerUpdate(BaseModel):
    part_number: Optional[str] = None
    content_length: Optional[str] = None
    content_md5: Optional[str] = None

class DocumentupdaterequestdatamultipartsinnerDb(BaseModel):
    part_number: Optional[str] = None
    content_length: Optional[str] = None
    content_md5: Optional[str] = None

