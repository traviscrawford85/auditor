from typing import Optional

from pydantic import BaseModel


class TextsnippetupdaterequestdataIn(BaseModel):
    phrase: Optional[str] = None
    snippet: Optional[str] = None
    whole_word: Optional[str] = None

class TextsnippetupdaterequestdataOut(BaseModel):
    phrase: Optional[str] = None
    snippet: Optional[str] = None
    whole_word: Optional[str] = None

class TextsnippetupdaterequestdataUpdate(BaseModel):
    phrase: Optional[str] = None
    snippet: Optional[str] = None
    whole_word: Optional[str] = None

class TextsnippetupdaterequestdataDb(BaseModel):
    phrase: Optional[str] = None
    snippet: Optional[str] = None
    whole_word: Optional[str] = None

