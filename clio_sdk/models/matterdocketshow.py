from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MatterdocketShowIn(BaseModel):
    data: Matterdocket

class MatterdocketShowOut(BaseModel):
    data: Matterdocket

class MatterdocketShowUpdate(BaseModel):
    data: Matterdocket

class MatterdocketShowDb(BaseModel):
    data: Matterdocket

