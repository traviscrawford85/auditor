from typing import Literal, cast

DiscountBaseType = Literal["money", "percentage"]

DISCOUNT_BASE_TYPE_VALUES: set[DiscountBaseType] = {
    "money",
    "percentage",
}


def check_discount_base_type(value: str) -> DiscountBaseType:
    if value in DISCOUNT_BASE_TYPE_VALUES:
        return cast(DiscountBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DISCOUNT_BASE_TYPE_VALUES!r}")
