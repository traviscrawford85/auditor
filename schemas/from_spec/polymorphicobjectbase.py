from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PolymorphicobjectbaseIn(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    identifier: Optional[str] = None
    secondary_identifier: Optional[str] = None
    tertiary_identifier: Optional[str] = None

class PolymorphicobjectbaseOut(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    identifier: Optional[str] = None
    secondary_identifier: Optional[str] = None
    tertiary_identifier: Optional[str] = None

class PolymorphicobjectbaseUpdate(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    identifier: Optional[str] = None
    secondary_identifier: Optional[str] = None
    tertiary_identifier: Optional[str] = None

class PolymorphicobjectbaseDb(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    identifier: Optional[str] = None
    secondary_identifier: Optional[str] = None
    tertiary_identifier: Optional[str] = None

