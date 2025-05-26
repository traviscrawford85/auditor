from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentcategoryShowIn(BaseModel):
    data: Documentcategory

class DocumentcategoryShowOut(BaseModel):
    data: Documentcategory

class DocumentcategoryShowUpdate(BaseModel):
    data: Documentcategory

class DocumentcategoryShowDb(BaseModel):
    data: Documentcategory

