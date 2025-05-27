from typing import Optional

from pydantic import BaseModel


class BillingsettingBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    rounded_duration: Optional[float] = None
    rounding: Optional[int] = None
    use_decimal_rounding: Optional[bool] = None
    currency: Optional[str] = None
    currency_sign: Optional[str] = None
    tax_rate: Optional[float] = None
    tax_name: Optional[str] = None
    apply_tax_by_default: Optional[bool] = None
    time_on_flat_rate_contingency_matters_is_non_billable: Optional[bool] = None
    use_secondary_tax: Optional[bool] = None
    secondary_tax_rate: Optional[float] = None
    secondary_tax_rule: Optional[str] = None
    secondary_tax_name: Optional[str] = None
    notify_after_bill_created: Optional[bool] = None
    use_utbms_codes: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class BillingsettingBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    rounded_duration: Optional[float] = None
    rounding: Optional[int] = None
    use_decimal_rounding: Optional[bool] = None
    currency: Optional[str] = None
    currency_sign: Optional[str] = None
    tax_rate: Optional[float] = None
    tax_name: Optional[str] = None
    apply_tax_by_default: Optional[bool] = None
    time_on_flat_rate_contingency_matters_is_non_billable: Optional[bool] = None
    use_secondary_tax: Optional[bool] = None
    secondary_tax_rate: Optional[float] = None
    secondary_tax_rule: Optional[str] = None
    secondary_tax_name: Optional[str] = None
    notify_after_bill_created: Optional[bool] = None
    use_utbms_codes: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class BillingsettingBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    rounded_duration: Optional[float] = None
    rounding: Optional[int] = None
    use_decimal_rounding: Optional[bool] = None
    currency: Optional[str] = None
    currency_sign: Optional[str] = None
    tax_rate: Optional[float] = None
    tax_name: Optional[str] = None
    apply_tax_by_default: Optional[bool] = None
    time_on_flat_rate_contingency_matters_is_non_billable: Optional[bool] = None
    use_secondary_tax: Optional[bool] = None
    secondary_tax_rate: Optional[float] = None
    secondary_tax_rule: Optional[str] = None
    secondary_tax_name: Optional[str] = None
    notify_after_bill_created: Optional[bool] = None
    use_utbms_codes: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class BillingsettingBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    rounded_duration: Optional[float] = None
    rounding: Optional[int] = None
    use_decimal_rounding: Optional[bool] = None
    currency: Optional[str] = None
    currency_sign: Optional[str] = None
    tax_rate: Optional[float] = None
    tax_name: Optional[str] = None
    apply_tax_by_default: Optional[bool] = None
    time_on_flat_rate_contingency_matters_is_non_billable: Optional[bool] = None
    use_secondary_tax: Optional[bool] = None
    secondary_tax_rate: Optional[float] = None
    secondary_tax_rule: Optional[str] = None
    secondary_tax_name: Optional[str] = None
    notify_after_bill_created: Optional[bool] = None
    use_utbms_codes: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

