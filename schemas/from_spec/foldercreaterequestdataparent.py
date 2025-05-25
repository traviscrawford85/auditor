from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class FoldercreaterequestdataparentIn(BaseModel):
    id: int
    type: str

class FoldercreaterequestdataparentOut(BaseModel):
    id: int
    type: str

class FoldercreaterequestdataparentUpdate(BaseModel):
    id: int
    type: str

class FoldercreaterequestdataparentDb(BaseModel):
    id: int
    type: str

