from typing import List

from pydantic import BaseModel

from .contact import ContactOut


class ContactListIn(BaseModel):
    data: List[ContactIn]

class ContactListOut(BaseModel):
    data: List[ContactOut]

class ContactListUpdate(BaseModel):
    data: List[ContactUpdate]

class ContactListDb(BaseModel):
    data: List[ContactDb]

