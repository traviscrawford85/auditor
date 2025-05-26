from typing import Literal, cast

CustomFieldSetindexOrder = Literal[
    "id(asc)", "id(desc)", "name(asc)", "name(desc)", "parent_type(asc)", "parent_type(desc)"
]

CUSTOM_FIELD_SETINDEX_ORDER_VALUES: set[CustomFieldSetindexOrder] = {
    "id(asc)",
    "id(desc)",
    "name(asc)",
    "name(desc)",
    "parent_type(asc)",
    "parent_type(desc)",
}


def check_custom_field_setindex_order(value: str) -> CustomFieldSetindexOrder:
    if value in CUSTOM_FIELD_SETINDEX_ORDER_VALUES:
        return cast(CustomFieldSetindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELD_SETINDEX_ORDER_VALUES!r}")
