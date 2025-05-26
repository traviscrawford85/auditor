from typing import Literal, cast

CustomFieldSetcreateJsonBodyDataParentType = Literal["Contact", "Matter"]

CUSTOM_FIELD_SETCREATE_JSON_BODY_DATA_PARENT_TYPE_VALUES: set[CustomFieldSetcreateJsonBodyDataParentType] = {
    "Contact",
    "Matter",
}


def check_custom_field_setcreate_json_body_data_parent_type(value: str) -> CustomFieldSetcreateJsonBodyDataParentType:
    if value in CUSTOM_FIELD_SETCREATE_JSON_BODY_DATA_PARENT_TYPE_VALUES:
        return cast(CustomFieldSetcreateJsonBodyDataParentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELD_SETCREATE_JSON_BODY_DATA_PARENT_TYPE_VALUES!r}"
    )
