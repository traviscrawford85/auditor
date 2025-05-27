from typing import Optional

from pydantic import BaseModel


class ReportcreaterequestdatapracticeareaIn(BaseModel):
    id: Optional[str] = None

class ReportcreaterequestdatapracticeareaOut(BaseModel):
    id: Optional[str] = None

class ReportcreaterequestdatapracticeareaUpdate(BaseModel):
    id: Optional[str] = None

class ReportcreaterequestdatapracticeareaDb(BaseModel):
    id: Optional[str] = None

