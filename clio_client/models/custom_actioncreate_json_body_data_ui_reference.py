from typing import Literal, cast

CustomActioncreateJsonBodyDataUiReference = Literal[
    "activities/show", "contacts/show", "documents/show", "folders/show", "matters/show"
]

CUSTOM_ACTIONCREATE_JSON_BODY_DATA_UI_REFERENCE_VALUES: set[CustomActioncreateJsonBodyDataUiReference] = {
    "activities/show",
    "contacts/show",
    "documents/show",
    "folders/show",
    "matters/show",
}


def check_custom_actioncreate_json_body_data_ui_reference(value: str) -> CustomActioncreateJsonBodyDataUiReference:
    if value in CUSTOM_ACTIONCREATE_JSON_BODY_DATA_UI_REFERENCE_VALUES:
        return cast(CustomActioncreateJsonBodyDataUiReference, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CUSTOM_ACTIONCREATE_JSON_BODY_DATA_UI_REFERENCE_VALUES!r}"
    )
