from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CustomfieldsetListIn(BaseModel):
    data: List[Customfieldset]

class CustomfieldsetListOut(BaseModel):
    data: List[Customfieldset]

class CustomfieldsetListUpdate(BaseModel):
    data: List[Customfieldset]

class CustomfieldsetListDb(BaseModel):
    data: List[Customfieldset]

