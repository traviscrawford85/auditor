from typing import Literal, cast

ContactindexCustomFieldValues = Literal["<", "<=", "=", ">", ">="]

CONTACTINDEX_CUSTOM_FIELD_VALUES_VALUES: set[ContactindexCustomFieldValues] = {
    "<",
    "<=",
    "=",
    ">",
    ">=",
}


def check_contactindex_custom_field_values(value: str) -> ContactindexCustomFieldValues:
    if value in CONTACTINDEX_CUSTOM_FIELD_VALUES_VALUES:
        return cast(ContactindexCustomFieldValues, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACTINDEX_CUSTOM_FIELD_VALUES_VALUES!r}")
