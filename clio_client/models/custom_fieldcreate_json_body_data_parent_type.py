from typing import Literal, cast

CustomFieldcreateJsonBodyDataParentType = Literal["Contact", "Matter"]

CUSTOM_FIELDCREATE_JSON_BODY_DATA_PARENT_TYPE_VALUES: set[CustomFieldcreateJsonBodyDataParentType] = {
    "Contact",
    "Matter",
}


def check_custom_fieldcreate_json_body_data_parent_type(value: str) -> CustomFieldcreateJsonBodyDataParentType:
    if value in CUSTOM_FIELDCREATE_JSON_BODY_DATA_PARENT_TYPE_VALUES:
        return cast(CustomFieldcreateJsonBodyDataParentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELDCREATE_JSON_BODY_DATA_PARENT_TYPE_VALUES!r}"
    )
