from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TextsnippetShowIn(BaseModel):
    data: Textsnippet

class TextsnippetShowOut(BaseModel):
    data: Textsnippet

class TextsnippetShowUpdate(BaseModel):
    data: Textsnippet

class TextsnippetShowDb(BaseModel):
    data: Textsnippet

