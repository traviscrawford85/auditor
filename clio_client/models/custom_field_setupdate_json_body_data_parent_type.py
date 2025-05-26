from typing import Literal, cast

CustomFieldSetupdateJsonBodyDataParentType = Literal["Contact", "Matter"]

CUSTOM_FIELD_SETUPDATE_JSON_BODY_DATA_PARENT_TYPE_VALUES: set[CustomFieldSetupdateJsonBodyDataParentType] = {
    "Contact",
    "Matter",
}


def check_custom_field_setupdate_json_body_data_parent_type(value: str) -> CustomFieldSetupdateJsonBodyDataParentType:
    if value in CUSTOM_FIELD_SETUPDATE_JSON_BODY_DATA_PARENT_TYPE_VALUES:
        return cast(CustomFieldSetupdateJsonBodyDataParentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELD_SETUPDATE_JSON_BODY_DATA_PARENT_TYPE_VALUES!r}"
    )
