from typing import Literal, cast

PaymentProfileBaseInterestType = Literal["compound", "simple"]

PAYMENT_PROFILE_BASE_INTEREST_TYPE_VALUES: set[PaymentProfileBaseInterestType] = {
    "compound",
    "simple",
}


def check_payment_profile_base_interest_type(value: str) -> PaymentProfileBaseInterestType:
    if value in PAYMENT_PROFILE_BASE_INTEREST_TYPE_VALUES:
        return cast(PaymentProfileBaseInterestType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PAYMENT_PROFILE_BASE_INTEREST_TYPE_VALUES!r}")
