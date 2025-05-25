from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MatterdocketShowIn(BaseModel):
    data: Any

class MatterdocketShowOut(BaseModel):
    data: Any

class MatterdocketShowUpdate(BaseModel):
    data: Any

class MatterdocketShowDb(BaseModel):
    data: Any

