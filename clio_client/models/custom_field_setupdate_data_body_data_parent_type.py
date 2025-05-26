from typing import Literal, cast

CustomFieldSetupdateDataBodyDataParentType = Literal["Contact", "Matter"]

CUSTOM_FIELD_SETUPDATE_DATA_BODY_DATA_PARENT_TYPE_VALUES: set[CustomFieldSetupdateDataBodyDataParentType] = {
    "Contact",
    "Matter",
}


def check_custom_field_setupdate_data_body_data_parent_type(value: str) -> CustomFieldSetupdateDataBodyDataParentType:
    if value in CUSTOM_FIELD_SETUPDATE_DATA_BODY_DATA_PARENT_TYPE_VALUES:
        return cast(CustomFieldSetupdateDataBodyDataParentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELD_SETUPDATE_DATA_BODY_DATA_PARENT_TYPE_VALUES!r}"
    )
