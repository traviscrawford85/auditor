from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MyeventShowIn(BaseModel):
    data: Any

class MyeventShowOut(BaseModel):
    data: Any

class MyeventShowUpdate(BaseModel):
    data: Any

class MyeventShowDb(BaseModel):
    data: Any

