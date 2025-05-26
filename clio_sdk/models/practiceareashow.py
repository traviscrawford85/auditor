from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PracticeareaShowIn(BaseModel):
    data: Practicearea

class PracticeareaShowOut(BaseModel):
    data: Practicearea

class PracticeareaShowUpdate(BaseModel):
    data: Practicearea

class PracticeareaShowDb(BaseModel):
    data: Practicearea

