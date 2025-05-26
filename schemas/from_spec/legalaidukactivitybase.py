from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LegalaidukactivityBaseIn(BaseModel):
    activity_sub_category: Optional[str] = None
    advocacy: Optional[str] = None
    base_rate: Optional[str] = None
    bolt_ons: Optional[str] = None
    bolt_ons_summary: Optional[str] = None
    court: Optional[str] = None
    eligible_for_sqm: Optional[str] = None
    expert: Optional[str] = None
    form_of_civil_legal_service: Optional[str] = None
    id: Optional[str] = None
    is_custom_rate: Optional[str] = None
    json_key: Optional[str] = None
    region: Optional[str] = None
    tax_exclusive: Optional[str] = None
    uplift: Optional[str] = None
    user_type: Optional[str] = None

class LegalaidukactivityBaseOut(BaseModel):
    activity_sub_category: Optional[str] = None
    advocacy: Optional[str] = None
    base_rate: Optional[str] = None
    bolt_ons: Optional[str] = None
    bolt_ons_summary: Optional[str] = None
    court: Optional[str] = None
    eligible_for_sqm: Optional[str] = None
    expert: Optional[str] = None
    form_of_civil_legal_service: Optional[str] = None
    id: Optional[str] = None
    is_custom_rate: Optional[str] = None
    json_key: Optional[str] = None
    region: Optional[str] = None
    tax_exclusive: Optional[str] = None
    uplift: Optional[str] = None
    user_type: Optional[str] = None

class LegalaidukactivityBaseUpdate(BaseModel):
    activity_sub_category: Optional[str] = None
    advocacy: Optional[str] = None
    base_rate: Optional[str] = None
    bolt_ons: Optional[str] = None
    bolt_ons_summary: Optional[str] = None
    court: Optional[str] = None
    eligible_for_sqm: Optional[str] = None
    expert: Optional[str] = None
    form_of_civil_legal_service: Optional[str] = None
    id: Optional[str] = None
    is_custom_rate: Optional[str] = None
    json_key: Optional[str] = None
    region: Optional[str] = None
    tax_exclusive: Optional[str] = None
    uplift: Optional[str] = None
    user_type: Optional[str] = None

class LegalaidukactivityBaseDb(BaseModel):
    activity_sub_category: Optional[str] = None
    advocacy: Optional[str] = None
    base_rate: Optional[str] = None
    bolt_ons: Optional[str] = None
    bolt_ons_summary: Optional[str] = None
    court: Optional[str] = None
    eligible_for_sqm: Optional[str] = None
    expert: Optional[str] = None
    form_of_civil_legal_service: Optional[str] = None
    id: Optional[str] = None
    is_custom_rate: Optional[str] = None
    json_key: Optional[str] = None
    region: Optional[str] = None
    tax_exclusive: Optional[str] = None
    uplift: Optional[str] = None
    user_type: Optional[str] = None

