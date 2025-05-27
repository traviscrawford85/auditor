from typing import Optional

from pydantic import BaseModel


class ReportcreaterequestdataclientIn(BaseModel):
    id: Optional[str] = None

class ReportcreaterequestdataclientOut(BaseModel):
    id: Optional[str] = None

class ReportcreaterequestdataclientUpdate(BaseModel):
    id: Optional[str] = None

class ReportcreaterequestdataclientDb(BaseModel):
    id: Optional[str] = None

