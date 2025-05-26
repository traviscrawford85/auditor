from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillingsettingBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    rounded_duration: Optional[str] = None
    rounding: Optional[str] = None
    use_decimal_rounding: Optional[str] = None
    currency: Optional[str] = None
    currency_sign: Optional[str] = None
    tax_rate: Optional[str] = None
    tax_name: Optional[str] = None
    apply_tax_by_default: Optional[str] = None
    time_on_flat_rate_contingency_matters_is_non_billable: Optional[str] = None
    use_secondary_tax: Optional[str] = None
    secondary_tax_rate: Optional[str] = None
    secondary_tax_rule: Optional[str] = None
    secondary_tax_name: Optional[str] = None
    notify_after_bill_created: Optional[str] = None
    use_utbms_codes: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class BillingsettingBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    rounded_duration: Optional[str] = None
    rounding: Optional[str] = None
    use_decimal_rounding: Optional[str] = None
    currency: Optional[str] = None
    currency_sign: Optional[str] = None
    tax_rate: Optional[str] = None
    tax_name: Optional[str] = None
    apply_tax_by_default: Optional[str] = None
    time_on_flat_rate_contingency_matters_is_non_billable: Optional[str] = None
    use_secondary_tax: Optional[str] = None
    secondary_tax_rate: Optional[str] = None
    secondary_tax_rule: Optional[str] = None
    secondary_tax_name: Optional[str] = None
    notify_after_bill_created: Optional[str] = None
    use_utbms_codes: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class BillingsettingBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    rounded_duration: Optional[str] = None
    rounding: Optional[str] = None
    use_decimal_rounding: Optional[str] = None
    currency: Optional[str] = None
    currency_sign: Optional[str] = None
    tax_rate: Optional[str] = None
    tax_name: Optional[str] = None
    apply_tax_by_default: Optional[str] = None
    time_on_flat_rate_contingency_matters_is_non_billable: Optional[str] = None
    use_secondary_tax: Optional[str] = None
    secondary_tax_rate: Optional[str] = None
    secondary_tax_rule: Optional[str] = None
    secondary_tax_name: Optional[str] = None
    notify_after_bill_created: Optional[str] = None
    use_utbms_codes: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class BillingsettingBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    rounded_duration: Optional[str] = None
    rounding: Optional[str] = None
    use_decimal_rounding: Optional[str] = None
    currency: Optional[str] = None
    currency_sign: Optional[str] = None
    tax_rate: Optional[str] = None
    tax_name: Optional[str] = None
    apply_tax_by_default: Optional[str] = None
    time_on_flat_rate_contingency_matters_is_non_billable: Optional[str] = None
    use_secondary_tax: Optional[str] = None
    secondary_tax_rate: Optional[str] = None
    secondary_tax_rule: Optional[str] = None
    secondary_tax_name: Optional[str] = None
    notify_after_bill_created: Optional[str] = None
    use_utbms_codes: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

