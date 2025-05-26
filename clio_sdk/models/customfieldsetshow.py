from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CustomfieldsetShowIn(BaseModel):
    data: Customfieldset

class CustomfieldsetShowOut(BaseModel):
    data: Customfieldset

class CustomfieldsetShowUpdate(BaseModel):
    data: Customfieldset

class CustomfieldsetShowDb(BaseModel):
    data: Customfieldset

