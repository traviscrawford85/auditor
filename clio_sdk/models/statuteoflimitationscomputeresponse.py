
from pydantic import BaseModel


class StatuteoflimitationscomputeresponseIn(BaseModel):
    due_at: str

class StatuteoflimitationscomputeresponseOut(BaseModel):
    due_at: str

class StatuteoflimitationscomputeresponseUpdate(BaseModel):
    due_at: str

class StatuteoflimitationscomputeresponseDb(BaseModel):
    due_at: str

