from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TextsnippetShowIn(BaseModel):
    data: Any

class TextsnippetShowOut(BaseModel):
    data: Any

class TextsnippetShowUpdate(BaseModel):
    data: Any

class TextsnippetShowDb(BaseModel):
    data: Any

