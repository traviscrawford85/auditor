from typing import Optional

from pydantic import BaseModel


class TasktemplatecreaterequestdatatasktemplateListIn(BaseModel):
    id: Optional[str] = None

class TasktemplatecreaterequestdatatasktemplatelistOut(BaseModel):
    id: Optional[str] = None

class TasktemplatecreaterequestdatatasktemplatelistUpdate(BaseModel):
    id: Optional[str] = None

class TasktemplatecreaterequestdatatasktemplatelistDb(BaseModel):
    id: Optional[str] = None

