from typing import Literal, cast

LineItemupdateJsonBodyDataKind = Literal["Expense", "Product", "Service"]

LINE_ITEMUPDATE_JSON_BODY_DATA_KIND_VALUES: set[LineItemupdateJsonBodyDataKind] = {
    "Expense",
    "Product",
    "Service",
}


def check_line_itemupdate_json_body_data_kind(value: str) -> LineItemupdateJsonBodyDataKind:
    if value in LINE_ITEMUPDATE_JSON_BODY_DATA_KIND_VALUES:
        return cast(LineItemupdateJsonBodyDataKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LINE_ITEMUPDATE_JSON_BODY_DATA_KIND_VALUES!r}")
