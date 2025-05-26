from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ContactShowIn(BaseModel):
    data: Contact

class ContactShowOut(BaseModel):
    data: Contact

class ContactShowUpdate(BaseModel):
    data: Contact

class ContactShowDb(BaseModel):
    data: Contact

