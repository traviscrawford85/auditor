from typing import Literal, cast

LineItemupdateDataBodyDataKind = Literal["Expense", "Product", "Service"]

LINE_ITEMUPDATE_DATA_BODY_DATA_KIND_VALUES: set[LineItemupdateDataBodyDataKind] = {
    "Expense",
    "Product",
    "Service",
}


def check_line_itemupdate_data_body_data_kind(value: str) -> LineItemupdateDataBodyDataKind:
    if value in LINE_ITEMUPDATE_DATA_BODY_DATA_KIND_VALUES:
        return cast(LineItemupdateDataBodyDataKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LINE_ITEMUPDATE_DATA_BODY_DATA_KIND_VALUES!r}")
