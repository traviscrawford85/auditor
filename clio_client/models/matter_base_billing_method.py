from typing import Literal, cast

MatterBaseBillingMethod = Literal["contingency", "flat", "hourly"]

MATTER_BASE_BILLING_METHOD_VALUES: set[MatterBaseBillingMethod] = {
    "contingency",
    "flat",
    "hourly",
}


def check_matter_base_billing_method(value: str) -> MatterBaseBillingMethod:
    if value in MATTER_BASE_BILLING_METHOD_VALUES:
        return cast(MatterBaseBillingMethod, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MATTER_BASE_BILLING_METHOD_VALUES!r}")
