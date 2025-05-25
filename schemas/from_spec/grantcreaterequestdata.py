from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class GrantcreaterequestdataIn(BaseModel):
    name: Optional[str] = None

class GrantcreaterequestdataOut(BaseModel):
    name: Optional[str] = None

class GrantcreaterequestdataUpdate(BaseModel):
    name: Optional[str] = None

class GrantcreaterequestdataDb(BaseModel):
    name: Optional[str] = None

