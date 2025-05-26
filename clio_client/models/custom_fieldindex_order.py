from typing import Literal, cast

CustomFieldindexOrder = Literal[
    "display_order(asc)", "display_order(desc)", "id(asc)", "id(desc)", "name(asc)", "name(desc)"
]

CUSTOM_FIELDINDEX_ORDER_VALUES: set[CustomFieldindexOrder] = {
    "display_order(asc)",
    "display_order(desc)",
    "id(asc)",
    "id(desc)",
    "name(asc)",
    "name(desc)",
}


def check_custom_fieldindex_order(value: str) -> CustomFieldindexOrder:
    if value in CUSTOM_FIELDINDEX_ORDER_VALUES:
        return cast(CustomFieldindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELDINDEX_ORDER_VALUES!r}")
