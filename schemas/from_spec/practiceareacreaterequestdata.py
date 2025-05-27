from typing import Optional

from pydantic import BaseModel


class PracticeareacreaterequestdataIn(BaseModel):
    category: Optional[str] = None
    code: Optional[str] = None
    name: str

class PracticeareacreaterequestdataOut(BaseModel):
    category: Optional[str] = None
    code: Optional[str] = None
    name: str

class PracticeareacreaterequestdataUpdate(BaseModel):
    category: Optional[str] = None
    code: Optional[str] = None
    name: str

class PracticeareacreaterequestdataDb(BaseModel):
    category: Optional[str] = None
    code: Optional[str] = None
    name: str

