from typing import Literal, cast

BillableMatteridsCustomFieldValues = Literal["<", "<=", "=", ">", ">="]

BILLABLE_MATTERIDS_CUSTOM_FIELD_VALUES_VALUES: set[BillableMatteridsCustomFieldValues] = {
    "<",
    "<=",
    "=",
    ">",
    ">=",
}


def check_billable_matterids_custom_field_values(value: str) -> BillableMatteridsCustomFieldValues:
    if value in BILLABLE_MATTERIDS_CUSTOM_FIELD_VALUES_VALUES:
        return cast(BillableMatteridsCustomFieldValues, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILLABLE_MATTERIDS_CUSTOM_FIELD_VALUES_VALUES!r}")
