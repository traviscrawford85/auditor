
from pydantic import BaseModel

from .contact import ContactOut


class ContactShowIn(BaseModel):
    data: ContactIn

class ContactShowOut(BaseModel):
    data: ContactOut

class ContactShowUpdate(BaseModel):
    data: ContactUpdate

class ContactShowDb(BaseModel):
    data: ContactDb

