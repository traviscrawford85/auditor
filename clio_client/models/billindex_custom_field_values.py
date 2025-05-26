from typing import Literal, cast

BillindexCustomFieldValues = Literal["<", "<=", "=", ">", ">="]

BILLINDEX_CUSTOM_FIELD_VALUES_VALUES: set[BillindexCustomFieldValues] = {
    "<",
    "<=",
    "=",
    ">",
    ">=",
}


def check_billindex_custom_field_values(value: str) -> BillindexCustomFieldValues:
    if value in BILLINDEX_CUSTOM_FIELD_VALUES_VALUES:
        return cast(BillindexCustomFieldValues, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILLINDEX_CUSTOM_FIELD_VALUES_VALUES!r}")
