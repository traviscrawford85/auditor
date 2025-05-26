from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentcategoryListIn(BaseModel):
    data: List[Documentcategory]

class DocumentcategoryListOut(BaseModel):
    data: List[Documentcategory]

class DocumentcategoryListUpdate(BaseModel):
    data: List[Documentcategory]

class DocumentcategoryListDb(BaseModel):
    data: List[Documentcategory]

