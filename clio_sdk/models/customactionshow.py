from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CustomactionShowIn(BaseModel):
    data: Customaction

class CustomactionShowOut(BaseModel):
    data: Customaction

class CustomactionShowUpdate(BaseModel):
    data: Customaction

class CustomactionShowDb(BaseModel):
    data: Customaction

