from typing import Literal, cast

CustomFieldSetcreateDataBodyDataParentType = Literal["Contact", "Matter"]

CUSTOM_FIELD_SETCREATE_DATA_BODY_DATA_PARENT_TYPE_VALUES: set[CustomFieldSetcreateDataBodyDataParentType] = {
    "Contact",
    "Matter",
}


def check_custom_field_setcreate_data_body_data_parent_type(value: str) -> CustomFieldSetcreateDataBodyDataParentType:
    if value in CUSTOM_FIELD_SETCREATE_DATA_BODY_DATA_PARENT_TYPE_VALUES:
        return cast(CustomFieldSetcreateDataBodyDataParentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELD_SETCREATE_DATA_BODY_DATA_PARENT_TYPE_VALUES!r}"
    )
