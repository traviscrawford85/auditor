from typing import Literal, cast

BillableClientindexCustomFieldValues = Literal["<", "<=", "=", ">", ">="]

BILLABLE_CLIENTINDEX_CUSTOM_FIELD_VALUES_VALUES: set[BillableClientindexCustomFieldValues] = {
    "<",
    "<=",
    "=",
    ">",
    ">=",
}


def check_billable_clientindex_custom_field_values(value: str) -> BillableClientindexCustomFieldValues:
    if value in BILLABLE_CLIENTINDEX_CUSTOM_FIELD_VALUES_VALUES:
        return cast(BillableClientindexCustomFieldValues, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILLABLE_CLIENTINDEX_CUSTOM_FIELD_VALUES_VALUES!r}")
