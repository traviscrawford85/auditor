from typing import Literal, cast

CustomActionupdateJsonBodyDataUiReference = Literal[
    "activities/show", "contacts/show", "documents/show", "folders/show", "matters/show"
]

CUSTOM_ACTIONUPDATE_JSON_BODY_DATA_UI_REFERENCE_VALUES: set[CustomActionupdateJsonBodyDataUiReference] = {
    "activities/show",
    "contacts/show",
    "documents/show",
    "folders/show",
    "matters/show",
}


def check_custom_actionupdate_json_body_data_ui_reference(value: str) -> CustomActionupdateJsonBodyDataUiReference:
    if value in CUSTOM_ACTIONUPDATE_JSON_BODY_DATA_UI_REFERENCE_VALUES:
        return cast(CustomActionupdateJsonBodyDataUiReference, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CUSTOM_ACTIONUPDATE_JSON_BODY_DATA_UI_REFERENCE_VALUES!r}"
    )
