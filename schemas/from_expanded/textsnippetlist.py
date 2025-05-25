from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TextsnippetListIn(BaseModel):
    data: List[Any]

class TextsnippetListOut(BaseModel):
    data: List[Any]

class TextsnippetListUpdate(BaseModel):
    data: List[Any]

class TextsnippetListDb(BaseModel):
    data: List[Any]

