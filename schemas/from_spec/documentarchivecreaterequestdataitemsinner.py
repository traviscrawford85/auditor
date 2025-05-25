from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentarchivecreaterequestdataitemsinnerIn(BaseModel):
    id: int
    type: int

class DocumentarchivecreaterequestdataitemsinnerOut(BaseModel):
    id: int
    type: int

class DocumentarchivecreaterequestdataitemsinnerUpdate(BaseModel):
    id: int
    type: int

class DocumentarchivecreaterequestdataitemsinnerDb(BaseModel):
    id: int
    type: int

