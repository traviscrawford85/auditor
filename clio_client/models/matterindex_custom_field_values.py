from typing import Literal, cast

MatterindexCustomFieldValues = Literal["<", "<=", "=", ">", ">="]

MATTERINDEX_CUSTOM_FIELD_VALUES_VALUES: set[MatterindexCustomFieldValues] = {
    "<",
    "<=",
    "=",
    ">",
    ">=",
}


def check_matterindex_custom_field_values(value: str) -> MatterindexCustomFieldValues:
    if value in MATTERINDEX_CUSTOM_FIELD_VALUES_VALUES:
        return cast(MatterindexCustomFieldValues, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MATTERINDEX_CUSTOM_FIELD_VALUES_VALUES!r}")
