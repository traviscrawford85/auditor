from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CustomfieldShowIn(BaseModel):
    data: Customfield

class CustomfieldShowOut(BaseModel):
    data: Customfield

class CustomfieldShowUpdate(BaseModel):
    data: Customfield

class CustomfieldShowDb(BaseModel):
    data: Customfield

