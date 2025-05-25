from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LegalaidukcontactbaseIn(BaseModel):
    id: Optional[str] = None
    disability: Optional[str] = None
    disability_code: Optional[str] = None
    ethnicity: Optional[str] = None
    ethnicity_title: Optional[str] = None
    financially_eligible: Optional[str] = None
    gender: Optional[str] = None
    gender_title: Optional[str] = None
    national_insurance_number: Optional[str] = None

class LegalaidukcontactbaseOut(BaseModel):
    id: Optional[str] = None
    disability: Optional[str] = None
    disability_code: Optional[str] = None
    ethnicity: Optional[str] = None
    ethnicity_title: Optional[str] = None
    financially_eligible: Optional[str] = None
    gender: Optional[str] = None
    gender_title: Optional[str] = None
    national_insurance_number: Optional[str] = None

class LegalaidukcontactbaseUpdate(BaseModel):
    id: Optional[str] = None
    disability: Optional[str] = None
    disability_code: Optional[str] = None
    ethnicity: Optional[str] = None
    ethnicity_title: Optional[str] = None
    financially_eligible: Optional[str] = None
    gender: Optional[str] = None
    gender_title: Optional[str] = None
    national_insurance_number: Optional[str] = None

class LegalaidukcontactbaseDb(BaseModel):
    id: Optional[str] = None
    disability: Optional[str] = None
    disability_code: Optional[str] = None
    ethnicity: Optional[str] = None
    ethnicity_title: Optional[str] = None
    financially_eligible: Optional[str] = None
    gender: Optional[str] = None
    gender_title: Optional[str] = None
    national_insurance_number: Optional[str] = None

