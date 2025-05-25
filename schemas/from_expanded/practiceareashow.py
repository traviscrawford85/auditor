from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PracticeareaShowIn(BaseModel):
    data: Any

class PracticeareaShowOut(BaseModel):
    data: Any

class PracticeareaShowUpdate(BaseModel):
    data: Any

class PracticeareaShowDb(BaseModel):
    data: Any

