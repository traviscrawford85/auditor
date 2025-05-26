from typing import Literal, cast

BillBaseType = Literal["ClientBill", "MatterBill"]

BILL_BASE_TYPE_VALUES: set[BillBaseType] = {
    "ClientBill",
    "MatterBill",
}


def check_bill_base_type(value: str) -> BillBaseType:
    if value in BILL_BASE_TYPE_VALUES:
        return cast(BillBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILL_BASE_TYPE_VALUES!r}")
