from typing import Literal, cast

LineItemBaseType = Literal["ActivityLineItem", "LineItem", "NoChargeLineItem", "SummaryLineItem"]

LINE_ITEM_BASE_TYPE_VALUES: set[LineItemBaseType] = {
    "ActivityLineItem",
    "LineItem",
    "NoChargeLineItem",
    "SummaryLineItem",
}


def check_line_item_base_type(value: str) -> LineItemBaseType:
    if value in LINE_ITEM_BASE_TYPE_VALUES:
        return cast(LineItemBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LINE_ITEM_BASE_TYPE_VALUES!r}")
