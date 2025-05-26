from typing import Literal, cast

InterestBaseType = Literal["compound", "simple"]

INTEREST_BASE_TYPE_VALUES: set[InterestBaseType] = {
    "compound",
    "simple",
}


def check_interest_base_type(value: str) -> InterestBaseType:
    if value in INTEREST_BASE_TYPE_VALUES:
        return cast(InterestBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INTEREST_BASE_TYPE_VALUES!r}")
