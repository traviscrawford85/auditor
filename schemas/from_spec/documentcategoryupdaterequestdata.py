from typing import Optional

from pydantic import BaseModel


class DocumentcategoryupdaterequestdataIn(BaseModel):
    name: Optional[str] = None

class DocumentcategoryupdaterequestdataOut(BaseModel):
    name: Optional[str] = None

class DocumentcategoryupdaterequestdataUpdate(BaseModel):
    name: Optional[str] = None

class DocumentcategoryupdaterequestdataDb(BaseModel):
    name: Optional[str] = None

