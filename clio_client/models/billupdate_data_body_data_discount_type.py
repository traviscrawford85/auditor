from typing import Literal, cast

BillupdateDataBodyDataDiscountType = Literal["money", "percentage"]

BILLUPDATE_DATA_BODY_DATA_DISCOUNT_TYPE_VALUES: set[BillupdateDataBodyDataDiscountType] = {
    "money",
    "percentage",
}


def check_billupdate_data_body_data_discount_type(value: str) -> BillupdateDataBodyDataDiscountType:
    if value in BILLUPDATE_DATA_BODY_DATA_DISCOUNT_TYPE_VALUES:
        return cast(BillupdateDataBodyDataDiscountType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILLUPDATE_DATA_BODY_DATA_DISCOUNT_TYPE_VALUES!r}")
