from typing import Literal, cast

BalanceBaseType = Literal["Client", "Matter"]

BALANCE_BASE_TYPE_VALUES: set[BalanceBaseType] = {
    "Client",
    "Matter",
}


def check_balance_base_type(value: str) -> BalanceBaseType:
    if value in BALANCE_BASE_TYPE_VALUES:
        return cast(BalanceBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BALANCE_BASE_TYPE_VALUES!r}")
