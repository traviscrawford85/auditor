from typing import Literal, cast

LineItemBaseKind = Literal["Expense", "Service"]

LINE_ITEM_BASE_KIND_VALUES: set[LineItemBaseKind] = {
    "Expense",
    "Service",
}


def check_line_item_base_kind(value: str) -> LineItemBaseKind:
    if value in LINE_ITEM_BASE_KIND_VALUES:
        return cast(LineItemBaseKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LINE_ITEM_BASE_KIND_VALUES!r}")
