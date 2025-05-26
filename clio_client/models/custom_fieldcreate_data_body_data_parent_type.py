from typing import Literal, cast

CustomFieldcreateDataBodyDataParentType = Literal["Contact", "Matter"]

CUSTOM_FIELDCREATE_DATA_BODY_DATA_PARENT_TYPE_VALUES: set[CustomFieldcreateDataBodyDataParentType] = {
    "Contact",
    "Matter",
}


def check_custom_fieldcreate_data_body_data_parent_type(value: str) -> CustomFieldcreateDataBodyDataParentType:
    if value in CUSTOM_FIELDCREATE_DATA_BODY_DATA_PARENT_TYPE_VALUES:
        return cast(CustomFieldcreateDataBodyDataParentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELDCREATE_DATA_BODY_DATA_PARENT_TYPE_VALUES!r}"
    )
