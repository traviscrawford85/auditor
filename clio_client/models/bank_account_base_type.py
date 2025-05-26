from typing import Literal, cast

BankAccountBaseType = Literal["Operating", "Trust"]

BANK_ACCOUNT_BASE_TYPE_VALUES: set[BankAccountBaseType] = {
    "Operating",
    "Trust",
}


def check_bank_account_base_type(value: str) -> BankAccountBaseType:
    if value in BANK_ACCOUNT_BASE_TYPE_VALUES:
        return cast(BankAccountBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BANK_ACCOUNT_BASE_TYPE_VALUES!r}")
