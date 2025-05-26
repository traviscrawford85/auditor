from typing import Literal, cast

CustomActionupdateFilesBodyDataUiReference = Literal[
    "activities/show", "contacts/show", "documents/show", "folders/show", "matters/show"
]

CUSTOM_ACTIONUPDATE_FILES_BODY_DATA_UI_REFERENCE_VALUES: set[CustomActionupdateFilesBodyDataUiReference] = {
    "activities/show",
    "contacts/show",
    "documents/show",
    "folders/show",
    "matters/show",
}


def check_custom_actionupdate_files_body_data_ui_reference(value: str) -> CustomActionupdateFilesBodyDataUiReference:
    if value in CUSTOM_ACTIONUPDATE_FILES_BODY_DATA_UI_REFERENCE_VALUES:
        return cast(CustomActionupdateFilesBodyDataUiReference, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CUSTOM_ACTIONUPDATE_FILES_BODY_DATA_UI_REFERENCE_VALUES!r}"
    )
