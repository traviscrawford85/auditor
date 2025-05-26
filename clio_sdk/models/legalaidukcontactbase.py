from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LegalaidukcontactBaseIn(BaseModel):
    id: Optional[int] = None
    disability: Optional[int] = None
    disability_code: Optional[str] = None
    ethnicity: Optional[int] = None
    ethnicity_title: Optional[str] = None
    financially_eligible: Optional[bool] = None
    gender: Optional[int] = None
    gender_title: Optional[str] = None
    national_insurance_number: Optional[str] = None

class LegalaidukcontactBaseOut(BaseModel):
    id: Optional[int] = None
    disability: Optional[int] = None
    disability_code: Optional[str] = None
    ethnicity: Optional[int] = None
    ethnicity_title: Optional[str] = None
    financially_eligible: Optional[bool] = None
    gender: Optional[int] = None
    gender_title: Optional[str] = None
    national_insurance_number: Optional[str] = None

class LegalaidukcontactBaseUpdate(BaseModel):
    id: Optional[int] = None
    disability: Optional[int] = None
    disability_code: Optional[str] = None
    ethnicity: Optional[int] = None
    ethnicity_title: Optional[str] = None
    financially_eligible: Optional[bool] = None
    gender: Optional[int] = None
    gender_title: Optional[str] = None
    national_insurance_number: Optional[str] = None

class LegalaidukcontactBaseDb(BaseModel):
    id: Optional[int] = None
    disability: Optional[int] = None
    disability_code: Optional[str] = None
    ethnicity: Optional[int] = None
    ethnicity_title: Optional[str] = None
    financially_eligible: Optional[bool] = None
    gender: Optional[int] = None
    gender_title: Optional[str] = None
    national_insurance_number: Optional[str] = None

