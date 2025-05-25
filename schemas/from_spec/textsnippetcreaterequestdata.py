from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TextsnippetcreaterequestdataIn(BaseModel):
    phrase: str
    snippet: str
    whole_word: Optional[str] = None

class TextsnippetcreaterequestdataOut(BaseModel):
    phrase: str
    snippet: str
    whole_word: Optional[str] = None

class TextsnippetcreaterequestdataUpdate(BaseModel):
    phrase: str
    snippet: str
    whole_word: Optional[str] = None

class TextsnippetcreaterequestdataDb(BaseModel):
    phrase: str
    snippet: str
    whole_word: Optional[str] = None

