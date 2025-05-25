from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CustomfieldmatterselectionbaseIn(BaseModel):
    id: Optional[str] = None
    display_number: Optional[str] = None

class CustomfieldmatterselectionbaseOut(BaseModel):
    id: Optional[str] = None
    display_number: Optional[str] = None

class CustomfieldmatterselectionbaseUpdate(BaseModel):
    id: Optional[str] = None
    display_number: Optional[str] = None

class CustomfieldmatterselectionbaseDb(BaseModel):
    id: Optional[str] = None
    display_number: Optional[str] = None

