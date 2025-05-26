from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumenttemplateShowIn(BaseModel):
    data: Documenttemplate

class DocumenttemplateShowOut(BaseModel):
    data: Documenttemplate

class DocumenttemplateShowUpdate(BaseModel):
    data: Documenttemplate

class DocumenttemplateShowDb(BaseModel):
    data: Documenttemplate

