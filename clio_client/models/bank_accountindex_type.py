from typing import Literal, cast

BankAccountindexType = Literal["OperatingAccount", "TrustAccount"]

BANK_ACCOUNTINDEX_TYPE_VALUES: set[BankAccountindexType] = {
    "OperatingAccount",
    "TrustAccount",
}


def check_bank_accountindex_type(value: str) -> BankAccountindexType:
    if value in BANK_ACCOUNTINDEX_TYPE_VALUES:
        return cast(BankAccountindexType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BANK_ACCOUNTINDEX_TYPE_VALUES!r}")
