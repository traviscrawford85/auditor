from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivityrateShowIn(BaseModel):
    data: Any

class ActivityrateShowOut(BaseModel):
    data: Any

class ActivityrateShowUpdate(BaseModel):
    data: Any

class ActivityrateShowDb(BaseModel):
    data: Any

