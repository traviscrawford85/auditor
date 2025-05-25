from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class GrantfundingsourcecreaterequestdataIn(BaseModel):
    name: Optional[str] = None

class GrantfundingsourcecreaterequestdataOut(BaseModel):
    name: Optional[str] = None

class GrantfundingsourcecreaterequestdataUpdate(BaseModel):
    name: Optional[str] = None

class GrantfundingsourcecreaterequestdataDb(BaseModel):
    name: Optional[str] = None

