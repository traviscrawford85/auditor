from typing import Optional

from pydantic import BaseModel


class LegalaidukactivityBaseIn(BaseModel):
    activity_sub_category: Optional[str] = None
    advocacy: Optional[int] = None
    base_rate: Optional[float] = None
    court: Optional[int] = None
    eligible_for_sqm: Optional[bool] = None
    expert: Optional[int] = None
    form_of_civil_legal_service: Optional[int] = None
    id: Optional[int] = None
    is_custom_rate: Optional[bool] = None
    json_key: Optional[str] = None
    region: Optional[int] = None
    tax_exclusive: Optional[bool] = None
    uplift: Optional[float] = None
    user_type: Optional[int] = None

class LegalaidukactivityBaseOut(BaseModel):
    activity_sub_category: Optional[str] = None
    advocacy: Optional[int] = None
    base_rate: Optional[float] = None
    court: Optional[int] = None
    eligible_for_sqm: Optional[bool] = None
    expert: Optional[int] = None
    form_of_civil_legal_service: Optional[int] = None
    id: Optional[int] = None
    is_custom_rate: Optional[bool] = None
    json_key: Optional[str] = None
    region: Optional[int] = None
    tax_exclusive: Optional[bool] = None
    uplift: Optional[float] = None
    user_type: Optional[int] = None

class LegalaidukactivityBaseUpdate(BaseModel):
    activity_sub_category: Optional[str] = None
    advocacy: Optional[int] = None
    base_rate: Optional[float] = None
    court: Optional[int] = None
    eligible_for_sqm: Optional[bool] = None
    expert: Optional[int] = None
    form_of_civil_legal_service: Optional[int] = None
    id: Optional[int] = None
    is_custom_rate: Optional[bool] = None
    json_key: Optional[str] = None
    region: Optional[int] = None
    tax_exclusive: Optional[bool] = None
    uplift: Optional[float] = None
    user_type: Optional[int] = None

class LegalaidukactivityBaseDb(BaseModel):
    activity_sub_category: Optional[str] = None
    advocacy: Optional[int] = None
    base_rate: Optional[float] = None
    court: Optional[int] = None
    eligible_for_sqm: Optional[bool] = None
    expert: Optional[int] = None
    form_of_civil_legal_service: Optional[int] = None
    id: Optional[int] = None
    is_custom_rate: Optional[bool] = None
    json_key: Optional[str] = None
    region: Optional[int] = None
    tax_exclusive: Optional[bool] = None
    uplift: Optional[float] = None
    user_type: Optional[int] = None

