from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CustomfieldListIn(BaseModel):
    data: List[Customfield]

class CustomfieldListOut(BaseModel):
    data: List[Customfield]

class CustomfieldListUpdate(BaseModel):
    data: List[Customfield]

class CustomfieldListDb(BaseModel):
    data: List[Customfield]

