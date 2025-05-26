from typing import Literal, cast

BillupdateJsonBodyDataDiscountType = Literal["money", "percentage"]

BILLUPDATE_JSON_BODY_DATA_DISCOUNT_TYPE_VALUES: set[BillupdateJsonBodyDataDiscountType] = {
    "money",
    "percentage",
}


def check_billupdate_json_body_data_discount_type(value: str) -> BillupdateJsonBodyDataDiscountType:
    if value in BILLUPDATE_JSON_BODY_DATA_DISCOUNT_TYPE_VALUES:
        return cast(BillupdateJsonBodyDataDiscountType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILLUPDATE_JSON_BODY_DATA_DISCOUNT_TYPE_VALUES!r}")
