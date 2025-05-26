from typing import Literal, cast

BillableMatterindexCustomFieldValues = Literal["<", "<=", "=", ">", ">="]

BILLABLE_MATTERINDEX_CUSTOM_FIELD_VALUES_VALUES: set[BillableMatterindexCustomFieldValues] = {
    "<",
    "<=",
    "=",
    ">",
    ">=",
}


def check_billable_matterindex_custom_field_values(value: str) -> BillableMatterindexCustomFieldValues:
    if value in BILLABLE_MATTERINDEX_CUSTOM_FIELD_VALUES_VALUES:
        return cast(BillableMatterindexCustomFieldValues, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILLABLE_MATTERINDEX_CUSTOM_FIELD_VALUES_VALUES!r}")
