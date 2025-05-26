from typing import Literal, cast

CustomActionupdateDataBodyDataUiReference = Literal[
    "activities/show", "contacts/show", "documents/show", "folders/show", "matters/show"
]

CUSTOM_ACTIONUPDATE_DATA_BODY_DATA_UI_REFERENCE_VALUES: set[CustomActionupdateDataBodyDataUiReference] = {
    "activities/show",
    "contacts/show",
    "documents/show",
    "folders/show",
    "matters/show",
}


def check_custom_actionupdate_data_body_data_ui_reference(value: str) -> CustomActionupdateDataBodyDataUiReference:
    if value in CUSTOM_ACTIONUPDATE_DATA_BODY_DATA_UI_REFERENCE_VALUES:
        return cast(CustomActionupdateDataBodyDataUiReference, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CUSTOM_ACTIONUPDATE_DATA_BODY_DATA_UI_REFERENCE_VALUES!r}"
    )
