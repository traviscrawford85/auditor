from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MyeventShowIn(BaseModel):
    data: Myevent

class MyeventShowOut(BaseModel):
    data: Myevent

class MyeventShowUpdate(BaseModel):
    data: Myevent

class MyeventShowDb(BaseModel):
    data: Myevent

