from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentcategorycreaterequestdataIn(BaseModel):
    name: str

class DocumentcategorycreaterequestdataOut(BaseModel):
    name: str

class DocumentcategorycreaterequestdataUpdate(BaseModel):
    name: str

class DocumentcategorycreaterequestdataDb(BaseModel):
    name: str

