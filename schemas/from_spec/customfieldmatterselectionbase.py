from typing import Optional

from pydantic import BaseModel


class CustomfieldmatterselectionBaseIn(BaseModel):
    id: Optional[str] = None
    display_number: Optional[str] = None

class CustomfieldmatterselectionBaseOut(BaseModel):
    id: Optional[str] = None
    display_number: Optional[str] = None

class CustomfieldmatterselectionBaseUpdate(BaseModel):
    id: Optional[str] = None
    display_number: Optional[str] = None

class CustomfieldmatterselectionBaseDb(BaseModel):
    id: Optional[str] = None
    display_number: Optional[str] = None

