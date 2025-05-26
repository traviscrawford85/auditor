from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PolymorphicobjectBaseIn(BaseModel):
    id: Optional[int] = None
    type: Optional[str] = None
    identifier: Optional[str] = None
    secondary_identifier: Optional[str] = None
    tertiary_identifier: Optional[str] = None

class PolymorphicobjectBaseOut(BaseModel):
    id: Optional[int] = None
    type: Optional[str] = None
    identifier: Optional[str] = None
    secondary_identifier: Optional[str] = None
    tertiary_identifier: Optional[str] = None

class PolymorphicobjectBaseUpdate(BaseModel):
    id: Optional[int] = None
    type: Optional[str] = None
    identifier: Optional[str] = None
    secondary_identifier: Optional[str] = None
    tertiary_identifier: Optional[str] = None

class PolymorphicobjectBaseDb(BaseModel):
    id: Optional[int] = None
    type: Optional[str] = None
    identifier: Optional[str] = None
    secondary_identifier: Optional[str] = None
    tertiary_identifier: Optional[str] = None

