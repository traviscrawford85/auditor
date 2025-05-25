from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CustomfieldmatterselectionIn(BaseModel):
    id: Optional[str] = None
    display_number: Optional[str] = None

class CustomfieldmatterselectionOut(BaseModel):
    id: Optional[str] = None
    display_number: Optional[str] = None

class CustomfieldmatterselectionUpdate(BaseModel):
    id: Optional[str] = None
    display_number: Optional[str] = None

class CustomfieldmatterselectionDb(BaseModel):
    id: Optional[str] = None
    display_number: Optional[str] = None

