from typing import Optional

from pydantic import BaseModel


class PracticeareaupdaterequestdataIn(BaseModel):
    category: Optional[str] = None
    code: Optional[str] = None
    name: Optional[str] = None

class PracticeareaupdaterequestdataOut(BaseModel):
    category: Optional[str] = None
    code: Optional[str] = None
    name: Optional[str] = None

class PracticeareaupdaterequestdataUpdate(BaseModel):
    category: Optional[str] = None
    code: Optional[str] = None
    name: Optional[str] = None

class PracticeareaupdaterequestdataDb(BaseModel):
    category: Optional[str] = None
    code: Optional[str] = None
    name: Optional[str] = None

