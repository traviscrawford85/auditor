from typing import Optional

from pydantic import BaseModel


class ReportcreaterequestdatamatterIn(BaseModel):
    id: Optional[str] = None

class ReportcreaterequestdatamatterOut(BaseModel):
    id: Optional[str] = None

class ReportcreaterequestdatamatterUpdate(BaseModel):
    id: Optional[str] = None

class ReportcreaterequestdatamatterDb(BaseModel):
    id: Optional[str] = None

