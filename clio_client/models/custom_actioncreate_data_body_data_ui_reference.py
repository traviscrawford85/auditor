from typing import Literal, cast

CustomActioncreateDataBodyDataUiReference = Literal[
    "activities/show", "contacts/show", "documents/show", "folders/show", "matters/show"
]

CUSTOM_ACTIONCREATE_DATA_BODY_DATA_UI_REFERENCE_VALUES: set[CustomActioncreateDataBodyDataUiReference] = {
    "activities/show",
    "contacts/show",
    "documents/show",
    "folders/show",
    "matters/show",
}


def check_custom_actioncreate_data_body_data_ui_reference(value: str) -> CustomActioncreateDataBodyDataUiReference:
    if value in CUSTOM_ACTIONCREATE_DATA_BODY_DATA_UI_REFERENCE_VALUES:
        return cast(CustomActioncreateDataBodyDataUiReference, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CUSTOM_ACTIONCREATE_DATA_BODY_DATA_UI_REFERENCE_VALUES!r}"
    )
