from typing import Literal, cast

CustomActioncreateFilesBodyDataUiReference = Literal[
    "activities/show", "contacts/show", "documents/show", "folders/show", "matters/show"
]

CUSTOM_ACTIONCREATE_FILES_BODY_DATA_UI_REFERENCE_VALUES: set[CustomActioncreateFilesBodyDataUiReference] = {
    "activities/show",
    "contacts/show",
    "documents/show",
    "folders/show",
    "matters/show",
}


def check_custom_actioncreate_files_body_data_ui_reference(value: str) -> CustomActioncreateFilesBodyDataUiReference:
    if value in CUSTOM_ACTIONCREATE_FILES_BODY_DATA_UI_REFERENCE_VALUES:
        return cast(CustomActioncreateFilesBodyDataUiReference, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CUSTOM_ACTIONCREATE_FILES_BODY_DATA_UI_REFERENCE_VALUES!r}"
    )
