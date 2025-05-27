from typing import Any, Optional

from pydantic import BaseModel


class UnnamedschemaIn(BaseModel):
    name: Optional[Any] = None
    value: Optional[Any] = None

class UnnamedschemaOut(BaseModel):
    name: Optional[Any] = None
    value: Optional[Any] = None

class UnnamedschemaUpdate(BaseModel):
    name: Optional[Any] = None
    value: Optional[Any] = None

class UnnamedschemaDb(BaseModel):
    name: Optional[Any] = None
    value: Optional[Any] = None

