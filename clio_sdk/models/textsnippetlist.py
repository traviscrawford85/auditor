from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TextsnippetListIn(BaseModel):
    data: List[Textsnippet]

class TextsnippetListOut(BaseModel):
    data: List[Textsnippet]

class TextsnippetListUpdate(BaseModel):
    data: List[Textsnippet]

class TextsnippetListDb(BaseModel):
    data: List[Textsnippet]

